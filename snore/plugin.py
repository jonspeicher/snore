"""This module contains the SnorePlugin class, which defines a Snarl plugin for the nose test 
runner.  It provides notification of test status and results using Snarl when nose is run."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import nose.plugins

# Many convenient things happen if your plugin class defines a docstring and calls the superclass in
# a few commonly-overridden methods (__init__, options, configure).  See the nose documentation.

class SnorePlugin(nose.plugins.Plugin):    
    """Enable Snarl notifications"""
    
    enabled = False
    name = "snore"
    score = 1
    
    def __init__(self, snarler, clock):
        super(SnorePlugin, self).__init__()
        self._snarler = snarler
        self._clock = clock
        
    def begin(self):
        self._start_time = self._clock.now()
        
    def finalize(self, result):
        title = self._get_test_title(result)
        body = self._elapsed_time(self._clock.now() - self._start_time)
        self._snarler.snarl(title, body)

    def _get_test_title(self, result):
        if result.errors:
            return self._test_summary(len(result.errors), result.testsRun, 'had errors.')
        elif result.failures:
            return self._test_summary(len(result.failures), result.testsRun, 'failed.')
        else:
            return self._test_summary(result.testsRun, result.testsRun, 'passed.')
            
    def _test_summary(self, count, total, summary):
        return str(count) + ' of ' + str(total) + ' test' + ('s ' if total > 1 else ' ') + summary
        
    def _elapsed_time(self, delta):
        return 'Tests completed in ' + self._format_delta(delta) + ' seconds.'
        
    def _format_delta(self, delta):
        return '%0.2f' % (delta.seconds + (delta.microseconds * 0.000001))