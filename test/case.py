"""This module contains the base class for the unit test cases for the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import doubles
import unittest

from snore.plugin import SnorePlugin

class SnorePluginTestCase(unittest.TestCase):
    def setUp(self):
        self._snarler = doubles.TestSnarler()
        self._clock = doubles.TestClock()
        self._plugin = SnorePlugin(self._snarler, self._clock)
        self._plugin.begin()  