"""This module contains unit tests for the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

# NOTE: These tests are intended to be run with nosetests, but they don't work with nosetests when
# the snore egg is installed in site-packages.  There is currently no way to run the tests directly
# from the command line by executing the test scripts.

import snore.plugin
import unittest

# Define a few test doubles.

class TestSnarler(object):
    def __init__(self):
        self.last_title = ''
    def snarl(self, title, body):
        self.last_title = title
        self.last_body = body
        
class TestResult(object):
    def __init__(self, num_tests_passed, num_tests_run):
        self.num_tests_passed = num_tests_passed
        self.testsRun = num_tests_run
    def wasSuccessful(self):
        return self.testsRun == self._num_tests_passed

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
        self.assertEqual("All unit tests passed.", self._snarler.last_title)
        
    def testGreenBodyContainsTotalTestCount(self):
        self._plugin.finalize(TestResult(5, 5))
        self.assertTrue(self._snarler.last_body.startswith("5 tests"))
        
    # TBD: Green body contains test count
    # testGreenBodyContainsTestRunTime
    # testRedTitleContainsNumberOfTestsFailed
    # testRedTitleContainsTotalTestCount
    # testRedBodyContainsTestRunTime
    # testErrorTitleContainsNumberOfTestsWithErrors
    # testErrorTitleContainsTotalTestCount
    # testErrorBodyContainsTestRunTime
    
    # TBD: Add to body first error or first failure text?