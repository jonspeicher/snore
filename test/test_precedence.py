"""This module contains unit tests for the precedence of output by the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

from case import SnorePluginTestCase
from doubles import TestResult

class TestSnorePluginFormatterPrecedence(SnorePluginTestCase):
    def testErrorsHavePrecedenceOverFailures(self):
        self._plugin.finalize(TestResult(run = 5, failed = 1, errors = 1))
        self.assertEqual('1 of 5 tests had errors.', self._snarler.last_title)
        
    # TBD: test icon precedence as well as title precedence?