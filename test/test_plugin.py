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
    def snarl(self, title):
        self.last_title = title
        
class TestResult(object):
    def __init__(self):
        self.successful = True
    def wasSuccessful(self):
        return self.successful

# This is the test case itself.
    
class TestSnorePlugin(unittest.TestCase):
    def setUp(self):
        self._snarler = TestSnarler()
        self._plugin = snore.plugin.SnorePlugin(self._snarler)
        self._results = TestResult()
        
    def testBeginIsQuiet(self):
        self._snarler.last_message = ''
        self._plugin.begin()
        self.assertEqual('', self._snarler.last_message)
    
    def testGreenTitleIsAllUnitTestsPassed(self):
        self._results.successful = True
        self._plugin.finalize(self._results)
        self.assertEqual("All unit tests passed.", self._snarler.last_title)
        
    # testGreenTitleContainsTotalTestCount
    # TBD: Green body contains test count
    # testGreenBodyContainsTestRunTime
    # testRedTitleContainsNumberOfTestsFailed
    # testRedTitleContainsTotalTestCount
    # testRedBodyContainsTestRunTime
    # testErrorTitleContainsNumberOfTestsWithErrors
    # testErrorTitleContainsTotalTestCount
    # testErrorBodyContainsTestRunTime
    
    # TBD: Add to body first error or first failure text?