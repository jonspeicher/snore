"""This module contains the Snarler class, which provides an interface for the snore plugin to use 
to display status and reports via Snarl in an uncomplicated fashion."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import PySnarl

class Snarler(object):
    """Interface with Snarl to display status and reports"""
        
    def snarl(self, title, body, icon):
        PySnarl.snShowMessage(title, body, timeout = 5, iconPath = icon)