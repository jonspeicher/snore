"""This module contains unit tests for the icon displayed by the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

from util import SnorePluginTest
from util import TestResult    

class TestSnorePluginIconOutput(SnorePluginTest):
    def testGreenIconIsPassDotPng(self):
        self._plugin.finalize(TestResult(run = 1, failed = 0, errors = 0))
        self.assertTrue(self._snarler.last_icon.endswith('pass.png'))