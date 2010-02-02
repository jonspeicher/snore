"""This module contains unit tests for the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

# NOTE: These tests are intended to be run with nosetests, but they don't work with nosetests when
# the snore egg is installed in site-packages.  There is currently no way to run the tests directly
# from the command line by executing the test scripts.

import datetime
import re
import snore.plugin
import unittest

# Define a few test doubles.

class TestSnarler(object):
    def snarl(self, title, body):
        self.last_title = title
        self.last_body = body
        
class TestClock(object):
    def __init__(self, interval_us):
        self._now = datetime.datetime.now()
        self._interval = datetime.timedelta(microseconds = interval_us)
    def now(self):
        self._now += self._interval
        return self._now
        
class TestResult(object):
    def __init__(self, run = 0, failed = 0, errors = 0):
        self.testsRun = run
        self.failures = failed * [None]
        self.errors = errors * [None]

# This is the test case itself.
    
class TestSnorePlugin(unittest.TestCase):
    def setUp(self):
        self._snarler = TestSnarler()
        self._plugin = snore.plugin.SnorePlugin(self._snarler, TestClock(0))
        self._plugin.begin()
        
    def testBeginDoesNotSnarl(self):
        self._snarler.last_message = ''
        self._plugin.begin()
        self.assertEqual('', self._snarler.last_message)
    
    def testGreenTitleIsNumberOfTestsPassedForOneTest(self):
        self._plugin.finalize(TestResult(run = 1, failed = 0, errors = 0))
        self.assertEqual('1 of 1 test passed.', self._snarler.last_title)
    
    def testGreenTitleIsNumberOfTestsPassedForTwoTests(self):
        self._plugin.finalize(TestResult(run = 2, failed = 0, errors = 0))
        self.assertEqual('2 of 2 tests passed.', self._snarler.last_title)
        
    def testGreenTitleIsNumberOfTestsPassedForSeveralTests(self):
        self._plugin.finalize(TestResult(run = 5, failed = 0, errors = 0))
        self.assertEqual('5 of 5 tests passed.', self._snarler.last_title)
        
    def testGreenBodyIsTestRunTime(self):
        regex = re.compile('Tests completed in \d+\.?\d* seconds.$')
        self._plugin.finalize(TestResult(run = 5, failed = 0, errors = 0))
        self.assertTrue(regex.search(self._snarler.last_body))
        
    def testRedTitleIsNumberOfTestsFailedForOneTest(self):
        self._plugin.finalize(TestResult(run = 1, failed = 1, errors = 0))
        self.assertEqual('1 of 1 test failed.', self._snarler.last_title)

    def testRedTitleIsNumberOfTestsFailedForTwoTests(self):
        self._plugin.finalize(TestResult(run = 2, failed = 2, errors = 0))
        self.assertEqual('2 of 2 tests failed.', self._snarler.last_title)
          
    def testRedTitleIsNumberOfTestsFailedForSeveralTests(self):
        self._plugin.finalize(TestResult(run = 5, failed = 3, errors = 0))
        self.assertEqual('3 of 5 tests failed.', self._snarler.last_title)
        
    def testRedBodyIsTestRunTime(self):
        regex = re.compile('Tests completed in \d+\.?\d* seconds.$')
        self._plugin.finalize(TestResult(run = 5, failed = 3, errors = 0))
        self.assertTrue(regex.search(self._snarler.last_body))
    
    def testErrorTitleIsNumberOfErrorsForOneTest(self):
        self._plugin.finalize(TestResult(run = 1, failed = 0, errors = 1))
        self.assertEqual('1 of 1 test had errors.', self._snarler.last_title)
        
    def testErrorTitleIsNumberOfErrorsForTwoTests(self):
        self._plugin.finalize(TestResult(run = 2, failed = 0, errors = 2))
        self.assertEqual('2 of 2 tests had errors.', self._snarler.last_title)

    def testErrorTitleIsNumberOfErrorsForSeveralTests(self):
        self._plugin.finalize(TestResult(run = 5, failed = 0, errors = 3))
        self.assertEqual('3 of 5 tests had errors.', self._snarler.last_title)
                
    def testErrorBodyIsTestRunTime(self):
        regex = re.compile('Tests completed in \d+\.?\d* seconds.$')
        self._plugin.finalize(TestResult(run = 5, failed = 0, errors = 3))
        self.assertTrue(regex.search(self._snarler.last_body))
        
    def testErrorsHavePrecedenceOverFailures(self):
        self._plugin.finalize(TestResult(run = 5, failed = 1, errors = 1))
        self.assertEqual('1 of 5 tests had errors.', self._snarler.last_title)
    
    def testZeroTimeElapsedComputationIsCorrect(self):
        self._plugin = snore.plugin.SnorePlugin(self._snarler, TestClock(0))
        self._plugin.begin()
        self._plugin.finalize(TestResult(run = 5, failed = 0, errors = 0))
        self.assertEqual('Tests completed in 0.00 seconds.', self._snarler.last_body)
        
    def testTenMsTimeElapsedComputationIsCorrect(self):
        self._plugin = snore.plugin.SnorePlugin(self._snarler, TestClock(10000))
        self._plugin.begin()
        self._plugin.finalize(TestResult(run = 5, failed = 0, errors = 0))
        self.assertEqual('Tests completed in 0.01 seconds.', self._snarler.last_body)
        
    def testTenthSecondTimeElapsedComputationIsCorrect(self):
        self._plugin = snore.plugin.SnorePlugin(self._snarler, TestClock(100000))
        self._plugin.begin()
        self._plugin.finalize(TestResult(run = 5, failed = 0, errors = 0))
        self.assertEqual('Tests completed in 0.10 seconds.', self._snarler.last_body)
        
    def testTwoSecondTimeElapsedComputationIsCorrect(self):
        self._plugin = snore.plugin.SnorePlugin(self._snarler, TestClock(2000000))
        self._plugin.begin()
        self._plugin.finalize(TestResult(run = 5, failed = 0, errors = 0))
        self.assertEqual('Tests completed in 2.00 seconds.', self._snarler.last_body)
        
    # TBD: Test images passed to snarler    