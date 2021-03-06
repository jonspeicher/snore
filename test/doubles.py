"""This module contains test doubles used by the unit tests for the SnorePlugin class."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import datetime

class TestSnarler(object):
    """Test double for snore's Snarler object"""
    def snarl(self, title, body, icon = ''):
        self.last_title = title
        self.last_body = body
        self.last_icon = icon
        
class TestClock(object):
    """Test double for a datetime.datetime object"""
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
    """Test double for nose's test result object"""
    def __init__(self, run = 0, failed = 0, errors = 0):
        self.testsRun = run
        self.failures = failed * [None]
        self.errors = errors * [None]