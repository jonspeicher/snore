"""This module contains the Formatter class, which formats nose test results for display by the
plugin."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

class Formatter(object):
    """Format test results for display"""
    
    def format_result(self, run, failed, errors):
        if errors:
            return self._summarize(errors, run, 'had errors.')
        elif failed:
            return self._summarize(failed, run, 'failed.')
        else:
            return self._summarize(run, run, 'passed.')
            
    def format_time(self, delta):
        return 'Tests completed in ' + self._format_delta(delta) + ' seconds.'
        
    def _format_delta(self, delta):
        return '%0.2f' % (delta.seconds + (delta.microseconds * 0.000001))
            
    def _summarize(self, count, total, summary):
        return str(count) + ' of ' + str(total) + ' test' + ('s ' if total > 1 else ' ') + summary