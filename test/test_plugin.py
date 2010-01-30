"""This test is intended to be run from the project root using nosetests.
For some reason nosetests breaks with the snore egg installed in site-packages.
Uninstall the snore egg for this test to work."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import sys
import unittest

def print_instructions_and_exit():    
    print __doc__
    exit(-1)
    
try:
    import snore.plugin
except ImportError:
    print_instructions_and_exit()
        
class TestSnorePlugin(unittest.TestCase):
    def setUp(self):
        try:
            self._plugin = snore.plugin.SnorePlugin()
        except AttributeError:
            print_instructions_and_exit()
        
    def testFoo(self):
        self.assertTrue(True)

if __name__ == '__main__':
    print_instructions_and_exit()