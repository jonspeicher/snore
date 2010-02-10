"""This module contains the Formatter class, which formats test results for display."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

class Formatter(object):
    """Format test results for display"""
    
    def __init__(self, icon_path):
        self._icon_path = icon_path
        
    def format_result(self, run, failed, errors):
        if errors:
            return (self._summary(errors, run, 'had errors.'), self._icon('error'))
        elif failed:
            return (self._summary(failed, run, 'failed.'), self._icon('fail'))
        else:
            return (self._summary(run, run, 'passed.'), self._icon('pass'))
            
    def format_time(self, delta):
        return 'Tests completed in ' + self._format_delta(delta) + ' seconds.'
        
    def _format_delta(self, delta):
        return '%0.2f' % (delta.seconds + (delta.microseconds * 0.000001))
            
    def _summary(self, count, total, summary):
        return str(count) + ' of ' + str(total) + ' test' + ('s ' if total > 1 else ' ') + summary
        
    def _icon(self, filename):
        return self._icon_path + '/' + filename + '.png'