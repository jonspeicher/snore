"""This module contains unit tests for the precedence of output by the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

# NOTE: These tests are intended to be run with nosetests, but they don't work with nosetests when
# the snore egg is installed in site-packages.  There is currently no way to run the tests directly
# from the command line by executing the test scripts.

from util import SnorePluginTest
from util import TestResult

class TestSnorePluginFormatterPrecedence(SnorePluginTest):
    def testErrorsHavePrecedenceOverFailures(self):
        self._plugin.finalize(TestResult(run = 5, failed = 1, errors = 1))
        self.assertEqual('1 of 5 tests had errors.', self._snarler.last_title)