"""This module contains the SnorePlugin class, which defines a Snarl plugin for the nose test 
runner.  It will provide notification of test events via the Snarl system notification agent when 
nose is run."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import datetime
import nose.plugins
import snarler

# Many convenient things happen if your plugin class defines a docstring and calls the superclass in
# a few required methods.  See the nose documentation.

class SnorePlugin(nose.plugins.Plugin):    
    """Enable Snarl notifications"""
    
    enabled = False
    name = "snore"
    score = 1
    
    def __init__(self, snarler = snarler.Snarler()):
        super(SnorePlugin, self).__init__()
        self._snarler = snarler
    
    def options(self, parser, env):
        super(SnorePlugin, self).options(parser, env)
        
    def configure(self, options, conf):
        super(SnorePlugin, self).configure(options, conf)
        
    def begin(self):
        self._start_time = datetime.datetime.now()
        self._snarler.snarl('start time = ' + str(self._start_time))