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
        title = self._get_title_string(result)
        count = self._make_test_count_string(result.testsRun)
        time = self._make_elapsed_time_string(5.678)
        
        if result.errors:
            count = '2 errors'
        elif result.failures:
            count = str(len(result.failures)) + ' of ' + count + ' failed'
        
        self._snarler.snarl(title, count + time)
    
    def _get_title_string(self, result):
        if result.errors: return 'Some unit tests had errors.'
        elif result.failures: return 'Some unit tests failed.'
        else: return 'All unit tests passed.'

    def _make_test_count_string(self, count):
        return str(count) + (' test' if count == 1 else ' tests')
        
    def _make_elapsed_time_string(self, time):
        return ' run in ' + str(time) + ' seconds.'