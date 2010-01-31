"""This module contains tests for the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

# NOTE: These tests are intended to be run with nosetests, but they don't work with nosetests when
# the snore egg is installed in site-packages.  There is currently no way to run the tests directly
# from the command line by executing the test scripts.

import snore.plugin
import sys
import unittest

# Define a few test doubles.

class TestSnarler(object):
    def __init__(self):
        self.last_message = ''
    def snarl(self, message):
        self.last_message = message
        
class TestResult(object):
    def __init__(self):
        self.testsRun = 0

# This is the test case itself.
    
class TestSnorePlugin(unittest.TestCase):
    def setUp(self):
        self._snarler = TestSnarler()
        self._plugin = snore.plugin.SnorePlugin(self._snarler)
        
    def testBeginIsQuiet(self):
        self._snarler.last_message = ''
        self._plugin.begin()
        self.assertEqual('', self._snarler.last_message)
    
    def testGreenTitleContainsNumberOfTestsPassed(self):
        pass
        #result = TestResult()
        #result.testsRun = 5
        #self._plugin.finalize(TestResult())
        #self.assertTrue(self._plugin.last_title.endswith('of 5 passed')
        
    # testGreenTitleContainsTotalTestCount
    # testGreenBodyContainsTestRunTime
    # testRedTitleContainsNumberOfTestsFailed
    # testRedTitleContainsTotalTestCount
    # testRedBodyContainsTestRunTime
    # testErrorTitleContainsNumberOfTestsWithErrors
    # testErrorTitleContainsTotalTestCount
    # testErrorBodyContainsTestRunTime
    
    # TBD: Add to body first error or first failure text?