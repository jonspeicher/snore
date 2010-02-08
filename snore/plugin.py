"""This module contains the SnorePlugin class, which defines a Snarl plugin for the nose test 
runner.  It provides notification of test status and results using Snarl when nose is run."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import nose.plugins
from formatter import Formatter

# Many convenient things happen if your plugin class defines a docstring and calls the superclass in
# a few commonly-overridden methods (__init__, options, configure).  See the nose documentation.

# TBD: http://peak.telecommunity.com/DevCenter/PkgResources#resource-extraction
# Who retrieves the filenames?  The plugin?  Does it give them to the Formatter?  Does the
# formatter return them?
# Also clean up temporary files when plugin is destroyed?

class SnorePlugin(nose.plugins.Plugin):    
    """Enable Snarl notifications"""
    
    enabled = False
    name = "snore"
    score = 1
    
    def __init__(self, snarler, clock):
        super(SnorePlugin, self).__init__()
        self._formatter = Formatter()
        self._snarler = snarler
        self._clock = clock
        
    def begin(self):
        self._start_time = self._clock.now()
        
    def finalize(self, result):
        counts = self._get_counts(result)
        title = self._formatter.format_result(*counts)
        body = self._formatter.format_time(self._clock.now() - self._start_time)
        self._snarler.snarl(title, body, 'pass.png')
        
    def _get_counts(self, result):
        return (result.testsRun, len(result.failures), len(result.errors))