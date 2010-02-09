"""This module contains unit tests for the icon displayed by the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import pkg_resources

from case import SnorePluginTestCase
from doubles import TestResult    

class TestSnorePluginIconOutput(SnorePluginTestCase):
    def setUp(self):
        super(TestSnorePluginIconOutput, self).setUp()
        self._package_path = pkg_resources.resource_filename('snore', 'icons/')
        
    def testGreenIconIsPassDotPng(self):
        self._plugin.finalize(TestResult(run = 1, failed = 0, errors = 0))
        self.assertTrue(self._snarler.last_icon.endswith('pass.png'))
        
    def testGreenIconHasPackagePath(self):
        self._plugin.finalize(TestResult(run = 1, failed = 0, errors = 0))
        self.assertTrue(self._snarler.last_icon.startswith(self._package_path))
        
    def testRedIconIsFailDotPng(self):
        self._plugin.finalize(TestResult(run = 1, failed = 1, errors = 0))
        self.assertTrue(self._snarler.last_icon.endswith('fail.png'))
        
    def testErrorIconIsErrorDotPng(self):
        self._plugin.finalize(TestResult(run = 1, failed = 0, errors = 1))
        self.assertTrue(self._snarler.last_icon.endswith('error.png'))
        