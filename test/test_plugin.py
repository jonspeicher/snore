"""This module contains unit tests for the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

# NOTE: These tests are intended to be run with nosetests, but they don't work with nosetests when
# the snore egg is installed in site-packages.  There is currently no way to run the tests directly
# from the command line by executing the test scripts.

import re
import snore.plugin
import unittest

# Define a few test doubles.

class TestSnarler(object):
    def __init__(self):
        self.last_title = ''
    def snarl(self, title, body = ''):
        self.last_title = title
        self.last_body = body
        
class TestResult(object):
    def __init__(self, num_tests_passed, num_tests_run, num_errors = 0):
        self.testsRun = num_tests_run
        self.failures = (num_tests_run - num_tests_passed) * [None]
        self.errors = num_errors * [None]

# This is the test case itself.
    
class TestSnorePlugin(unittest.TestCase):
    def setUp(self):
        self._snarler = TestSnarler()
        self._plugin = snore.plugin.SnorePlugin(self._snarler)
        
    def testBeginDoesNotSnarl(self):
        self._snarler.last_message = ''
        self._plugin.begin()
        self.assertEqual('', self._snarler.last_message)
    
    def testGreenTitleIsAllUnitTestsPassed(self):
        self._plugin.finalize(TestResult(5, 5))
        self.assertEqual('All unit tests passed.', self._snarler.last_title)
    
    def testGreenBodyStartsWithTotalTestCountForOneTest(self):
        self._plugin.finalize(TestResult(1, 1))
        self.assertTrue(self._snarler.last_body.startswith('1 of 1 test passed'))
    
    def testGreenBodyStartsWithTotalTestCountForTwoTests(self):
        self._plugin.finalize(TestResult(2, 2))
        self.assertTrue(self._snarler.last_body.startswith('2 of 2 tests passed'))
        
    def testGreenBodyStartsWithTotalTestCountForSeveralTests(self):
        self._plugin.finalize(TestResult(5, 5))
        self.assertTrue(self._snarler.last_body.startswith('5 of 5 tests passed'))
        
    def testGreenBodyEndsWithTestRunTime(self):
        regex = re.compile(' in \d+\.?\d* seconds.$')
        self._plugin.finalize(TestResult(5, 5))
        self.assertTrue(regex.search(self._snarler.last_body))
        
    def testRedTitleIsSomeUnitTestsFailed(self):
        self._plugin.finalize(TestResult(3, 5))
        self.assertEqual('Some unit tests failed.', self._snarler.last_title)
    
    def testRedBodyStartsWithNumberOfTestsFailedForOneTest(self):
        self._plugin.finalize(TestResult(0, 1))
        self.assertTrue(self._snarler.last_body.startswith('1 of 1 test failed'))

    def testRedBodyStartsWithNumberOfTestsFailedForTwoTests(self):
        self._plugin.finalize(TestResult(0, 2))
        self.assertTrue(self._snarler.last_body.startswith('2 of 2 tests failed')) 
          
    def testRedBodyStartsWithNumberOfTestsFailedForSeveralTests(self):
        self._plugin.finalize(TestResult(2, 5))
        self.assertTrue(self._snarler.last_body.startswith('3 of 5 tests failed'))
        
    def testRedBodyEndsWithTestRunTime(self):
        regex = re.compile(' in \d+\.?\d* seconds.$')
        self._plugin.finalize(TestResult(3, 5))
        self.assertTrue(regex.search(self._snarler.last_body))
    
    def testErrorTitleIsSomeUnitTestsHadErrors(self):
        self._plugin.finalize(TestResult(3, 5, 2))
        self.assertEqual('Some unit tests had errors.', self._snarler.last_title)    
    
    def testErrorBodyStartsWithNumberOfErrorsForOneTest(self):
        self._plugin.finalize(TestResult(0, 1, 1))
        self.assertTrue(self._snarler.last_body.startswith('1 of 1 test had errors'))
        
    def testErrorBodyStartsWithNumberOfErrorsForTwoTests(self):
        self._plugin.finalize(TestResult(0, 2, 2))
        self.assertTrue(self._snarler.last_body.startswith('2 of 2 tests had errors'))

    def testErrorBodyStartsWithNumberOfErrorsForSeveralTests(self):
        self._plugin.finalize(TestResult(2, 5, 3))
        self.assertTrue(self._snarler.last_body.startswith('3 of 5 tests had errors'))
                
    def testErrorBodyEndsWithTestRunTime(self):
        regex = re.compile(' in \d+\.?\d* seconds.$')
        self._plugin.finalize(TestResult(3, 5, 2))
        self.assertTrue(regex.search(self._snarler.last_body))
    
    # TBD: Maybe add "testOneFailed..." and "testMultipleFailed..." tests to drive correctness
    # TBD: What does it do with zero tests?
    # TBD: Test that time computation is accurate with injected "clock"?
    # TBD: Test images passed to snarler
    # TBD: Add to body first error or first failure text, or name of first failing test case?
    # TBD: Also add a test case for the plugin using the framework? Ick.
    