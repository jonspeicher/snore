"""This module contains tests for the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

# NOTE: These tests are intended to be run with nosetests, but they don't work with nosetests when
# the snore egg is installed in site-packages.  There is currently no way to run the tests directly
# from the command line by executing the test scripts.

import snore.plugin
import sys
import unittest

class TestSnarler(object):
    def snarl(self, message):
        self.lastMessage = message
    
class TestSnorePlugin(unittest.TestCase):
    def setUp(self):
        self._snarler = TestSnarler()
        self._plugin = snore.plugin.SnorePlugin(self._snarler)
        
    def testBeginAnnouncesTestStartTime(self):
        self._plugin.begin()
        self.assertTrue(self._snarler.lastMessage.startswith("start time = "))