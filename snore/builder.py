"""This module contains a method to build the snore plugin, which is used as the nose entry point.  
This keeps the import of snarler (and thus PySnarl) out of the plugin so unit tests run on a Mac."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import plugin
import snarler

def build():
    return plugin.SnorePlugin(snarler.Snarler())