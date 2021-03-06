"""This module contains the SnorePlugin class, which defines a Snarl plugin for the nose test 
runner.  It provides notification of test status and results using Snarl when nose is run."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

from formatter import Formatter
import nose.plugins
import pkg_resources

# Many convenient things happen if your plugin class defines a docstring and calls the superclass in
# a few commonly-overridden methods (__init__, options, configure).  See the nose documentation.

class SnorePlugin(nose.plugins.Plugin):    
    """Enable Snarl notifications"""
    
    enabled = False
    name = "snore"
    score = 1
    
    def __init__(self, snarler, clock):
        super(SnorePlugin, self).__init__()
        self._formatter = Formatter(self._get_path('icons/'))
        self._snarler = snarler
        self._clock = clock
        
    def begin(self):
        self._start_time = self._clock.now()
        
    def finalize(self, result):
        counts = self._get_counts(result)
        title, icon = self._formatter.format_result(*counts)
        body = self._formatter.format_time(self._clock.now() - self._start_time)
        self._snarler.snarl(title, body, icon)
    
    def _get_counts(self, result):
        return (result.testsRun, len(result.failures), len(result.errors))
        
    def _get_path(self, filename):
        return pkg_resources.resource_filename('snore', filename)