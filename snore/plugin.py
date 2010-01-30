# snore
# Copyright (c) 2010 Jonathan Speicher
# jon.speicher@gmail.com
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

from nose.plugins import Plugin

"""
This class defines a Snarl plugin for the nose test runner.  It will provide notification of test
events via the Snarl system notification agent when nose is run.
"""

class SnorePlugin(Plugin):
    
    def options(self, parser, env):
        super(SnorePlugin, self).options(parser, env)
        
    def configure(self, options, conf):
        super(SnorePlugin, self).configure(options, conf)