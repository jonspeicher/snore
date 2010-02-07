"""This module contains unit tests for the text content output by the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

# NOTE: These tests are intended to be run with nosetests.  There is currently no way to run the 
# tests directly from the command line by executing the test scripts.

import re

from util import SnorePluginTest
from util import TestResult

class TestSnorePluginTextContent(SnorePluginTest):
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