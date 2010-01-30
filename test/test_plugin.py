"""This test is intended to be run from the project root using nosetests.
For some reason nosetests breaks with the snore egg installed in site-packages.
Uninstall the snore egg for this test to work."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

import sys
import unittest

# I can not for the life of me make this test work from nosetests when the egg is installed.  I'm
# sure it has to do with paths and such, but for now just add some restrictions.

def print_instructions_and_exit():    
    print __doc__
    exit(-1)

# Import will fail if the test is run from its current directory.

try:
    import snore.plugin
except ImportError:
    print_instructions_and_exit()

# Define a test double for the Snarler.

class TestSnarler(object):
    def snarl(self, message):
        self.lastMessage = message
    
# This is the test case itself (finally!).  The exception handler in setUp covers an exception that
# I see running nosetests in the source tree while the egg installed in site-packages.  It works
# fine in an interactive Python shell, but not with nosetests.

class TestSnorePlugin(unittest.TestCase):
    def setUp(self):
        try:
            self._snarler = TestSnarler()
            self._plugin = snore.plugin.SnorePlugin(self._snarler)
        except AttributeError:
            print_instructions_and_exit()
        
    def testBeginAnnouncesTestStartTime(self):
        self._plugin.begin()
        self.assertTrue(self._snarler.lastMessage.startswith("start time = "))

if __name__ == '__main__':
    print_instructions_and_exit()