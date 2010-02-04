"""This module contains unit tests for the accuracy of output by the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

# NOTE: These tests are intended to be run with nosetests, but they don't work with nosetests when
# the snore egg is installed in site-packages.  There is currently no way to run the tests directly
# from the command line by executing the test scripts.

from util import SnorePluginTest
from util import TestResult    

class TestSnorePluginElapsedTimeAccuracy(SnorePluginTest):
    def testZeroTimeElapsedComputationIsCorrect(self):
        self._clock.interval_ms = 0
        self._plugin.finalize(TestResult())
        self.assertEqual('Tests completed in 0.00 seconds.', self._snarler.last_body)
        
    def testTenMsTimeElapsedComputationIsCorrect(self):
        self._clock.interval_ms = 10
        self._plugin.finalize(TestResult())
        self.assertEqual('Tests completed in 0.01 seconds.', self._snarler.last_body)
        
    def testTenthSecondTimeElapsedComputationIsCorrect(self):
        self._clock.interval_ms = 100
        self._plugin.finalize(TestResult())
        self.assertEqual('Tests completed in 0.10 seconds.', self._snarler.last_body)
        
    def testTwoSecondTimeElapsedComputationIsCorrect(self):
        self._clock.interval_ms = 2000
        self._plugin.finalize(TestResult())
        self.assertEqual('Tests completed in 2.00 seconds.', self._snarler.last_body)