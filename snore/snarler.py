"""This module contains the Snarler class, which provides an interface for the snore plugin to use 
to display status and reports via Snarl in an uncomplicated fashion."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import logging

# TBD: Ensure this snarler matches the interface of the test snarler!!

class Snarler(object):
    """Interface with Snarl to display status and reports"""
    
    def __init__(self):
        self._logger = logging.getLogger('nose.plugins.snore')
        
    def snarl(self, title, body):
        self._logger.debug('snore ----------------------------------')
        self._logger.debug(title)
        self._logger.debug(body)