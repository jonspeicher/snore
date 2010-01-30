"""This module contains the Snarler class, which provides an interface for the Snore plugin to use 
to display status and reports via Snarl."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import logging

class Snarler(object):
    """Interface with Snarl to display status and reports"""
    
    def __init__(self):
        self._logger = logging.getLogger("nose.plugins.snore")
        
    def snarl(self, string):
        self._logger.debug(string)