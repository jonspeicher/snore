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
    
    def testGreenTitleIsNumberOfTestsPassedForOneTest(self):
        self._plugin.finalize(TestResult(1, 1))
        self.assertEqual('1 of 1 test passed.', self._snarler.last_title)
    
    def testGreenTitleIsNumberOfTestsPassedForTwoTests(self):
        self._plugin.finalize(TestResult(2, 2))
        self.assertEqual('2 of 2 tests passed.', self._snarler.last_title)
        
    def testGreenTitleIsNumberOfTestsPassedForSeveralTests(self):
        self._plugin.finalize(TestResult(5, 5))
        self.assertEqual('5 of 5 tests passed.', self._snarler.last_title)
        
    def testGreenBodyIsTestRunTime(self):
        regex = re.compile('Tests completed in \d+\.?\d* seconds.$')
        self._plugin.finalize(TestResult(5, 5))
        self.assertTrue(regex.search(self._snarler.last_body))
        
    def testRedTitleIsNumberOfTestsFailedForOneTest(self):
        self._plugin.finalize(TestResult(0, 1))
        self.assertEqual('1 of 1 test failed.', self._snarler.last_title)

    def testRedTitleIsNumberOfTestsFailedForTwoTests(self):
        self._plugin.finalize(TestResult(0, 2))
        self.assertEqual('2 of 2 tests failed.', self._snarler.last_title)
          
    def testRedTitleIsNumberOfTestsFailedForSeveralTests(self):
        self._plugin.finalize(TestResult(2, 5))
        self.assertEqual('3 of 5 tests failed.', self._snarler.last_title)
        
    def testRedBodyIsTestRunTime(self):
        regex = re.compile('Tests completed in \d+\.?\d* seconds.$')
        self._plugin.finalize(TestResult(3, 5))
        self.assertTrue(regex.search(self._snarler.last_body))
    
    def testErrorTitleIsNumberOfErrorsForOneTest(self):
        self._plugin.finalize(TestResult(0, 1, 1))
        self.assertEqual('1 of 1 test had errors.', self._snarler.last_title)
        
    def testErrorTitleIsNumberOfErrorsForTwoTests(self):
        self._plugin.finalize(TestResult(0, 2, 2))
        self.assertEqual('2 of 2 tests had errors.', self._snarler.last_title)

    def testErrorTitleIsNumberOfErrorsForSeveralTests(self):
        self._plugin.finalize(TestResult(2, 5, 3))
        self.assertEqual('3 of 5 tests had errors.', self._snarler.last_title)
                
    def testErrorBodyIsTestRunTime(self):
        regex = re.compile('Tests completed in \d+\.?\d* seconds.$')
        self._plugin.finalize(TestResult(3, 5, 2))
        self.assertTrue(regex.search(self._snarler.last_body))
    
    # TBD: What does it do with zero tests?
    # TBD: Test that time computation is accurate with injected "clock"?
    # TBD: Test images passed to snarler    