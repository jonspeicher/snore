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
        if result.errors:
            title = self._summary(len(result.errors), result.testsRun, 'had errors.')
        elif result.failures:
            title = self._summary(len(result.failures), result.testsRun, 'failed.')
        else:
            title = self._summary(result.testsRun, result.testsRun, 'passed.')
        print title
        time = self._elapsed_time(5.678)
        self._snarler.snarl(title, time)

    def _summary(self, count, total, postfix):
        return str(count) + ' of ' + str(total) + (' test ' if total == 1 else ' tests ') + postfix
        
    def _elapsed_time(self, time):
        return 'Tests completed in ' + str(time) + ' seconds.'