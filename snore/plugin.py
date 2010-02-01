"""This module contains the SnorePlugin class, which defines a Snarl plugin for the nose test 
runner.  It provides notification of test status and results using Snarl when nose is run."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import nose.plugins

# Many convenient things happen if your plugin class defines a docstring and calls the superclass in
# a few required methods.  See the nose documentation.

class SnorePlugin(nose.plugins.Plugin):    
    """Enable Snarl notifications"""
    
    enabled = False
    name = "snore"
    score = 1
    
    def __init__(self, snarler):
        super(SnorePlugin, self).__init__()
        self._snarler = snarler
    
    def options(self, parser, env):
        super(SnorePlugin, self).options(parser, env)
        
    def configure(self, options, conf):
        super(SnorePlugin, self).configure(options, conf)
        
    def begin(self):
        pass
        
    def finalize(self, result):
        if result.wasSuccessful():
            self._snarler.snarl('All unit tests passed.', '5 tests run in 5.678 seconds.')
        else:
            self._snarler.snarl('Some unit tests failed.', '3 of 5 tests failed')