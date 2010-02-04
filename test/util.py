"""This module contains utilities and classes used by the unit tests for the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

# NOTE: These tests are intended to be run with nosetests, but they don't work with nosetests when
# the snore egg is installed in site-packages.  There is currently no way to run the tests directly
# from the command line by executing the test scripts.

import datetime
import snore.plugin
import unittest

# Define a few test doubles.

class TestSnarler(object):
    def snarl(self, title, body):
        self.last_title = title
        self.last_body = body
        
class TestClock(object):
    def __init__(self):
        self._now = datetime.datetime.now()
        self.interval_ms = 0
    def now(self):
        self._now += self._interval
        return self._now
    def _set_interval_ms(self, interval_ms):
        self._interval = datetime.timedelta(microseconds = interval_ms * 1000)
    interval_ms = property(None, _set_interval_ms)
        
class TestResult(object):
    def __init__(self, run = 0, failed = 0, errors = 0):
        self.testsRun = run
        self.failures = failed * [None]
        self.errors = errors * [None]

# Define a base for all plugin test cases.

class SnorePluginTest(unittest.TestCase):
    def setUp(self):
        self._snarler = TestSnarler()
        self._clock = TestClock()
        self._plugin = snore.plugin.SnorePlugin(self._snarler, self._clock)
        self._plugin.begin()  