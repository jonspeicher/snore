"""This module contains unit tests for the accuracy of output by the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

from case import SnorePluginTestCase
from doubles import TestResult    

class TestSnorePluginElapsedTimeAccuracy(SnorePluginTestCase):
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