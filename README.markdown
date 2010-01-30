snore
=====

snore is a Snarl plugin for nose.

Description
-----------

Writing Python?  Stuck with Windows?  Get your TDD on with snore.  snore plugs in to the nose test runner and uses the [Growl](http://growl.info) clone Snarl to provide immediate feedback for your test results.  It is most fun and effective with a continuous test runner like [autonose](http://github.com/gfxmonk/autonose).

Requirements
------------

* Snarl (http://www.fullphat.net)
* PySnarl (http://code.google.com/p/pysnarl)
* nose (http://somethingaboutorange.com/mrl/projects/nose)

I've tested snore with Python 2.5, Snarl 2.21, PySnarl 1.0.2, and nose 0.11.1 on Windows XP Professional SP2 and on **nothing else**.  snore was largely developed (and its tests do run) with Python 2.6 on Mac OS X 10.6.2 (Snow Leopard), however.

Installation
------------

First, install the required dependencies.  Snarl must be installed according to its instructions.  nose can be retrieved and installed with `easy_install nose`.  To install PySnarl, download and unzip the source and run `setup.py install` from the unzipped source's root directory.

TBD: installing snore (python setup.py install --root=test, python setup.py install?  Or if it winds up on the PyPI, make that into build instructions?)

TBD: Features, descriptions, etc.
---------------------------------

TBD: running (nosetests --with-snore), changing pngs?

Tests
-----

TBD: talk about running tests in the source repo, weird restrictions

Author
------

Jon Speicher (jon.speicher@gmail.com)

Credits
-------

snore is pretty dumb.  For the most part, it simply ties together existing software, and so credit is due to the authors of Snarl, PySnarl, and nose.  Additionally, I spent a good chunk of time studying [NoseGrowl](http://www.assembla.com/wiki/show/nosegrowl) as an example.

License
-------

    The MIT License

    Copyright (c) 2010 Jonathan Speicher

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.