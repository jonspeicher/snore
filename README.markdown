snore
=====

snore is a Snarl notification plugin for Python's nose unit test runner.

Description
===========

Writing Python?  Stuck with Windows?  Get your TDD on with snore.  snore plugs in to the nose test runner and uses the [Growl](http://growl.info) clone Snarl to provide immediate feedback for your test results.  The snore plugin is most fun and effective with a continuous test runner like [autonose](http://github.com/gfxmonk/autonose).

Requirements
============

* setuptools (http://pypi.python.org/pypi/setuptools)
* Snarl (http://www.fullphat.net)
* PySnarl (http://code.google.com/p/pysnarl)
* nose (http://somethingaboutorange.com/mrl/projects/nose)

I've tested snore with Python 2.5, Snarl 2.21, PySnarl 1.0.2, and nose 0.11.1 on Windows XP Professional SP2 and on **nothing else**.  snore was largely developed using Python 2.6 on Mac OS X 10.6.2 (Snow Leopard), however, and the unit tests should run on that platform as well.

Installation
============

First, install the required dependencies.  Snarl must be installed according to the instructions found at its website.  Once `setuptools` is installed, nose can be retrieved and installed by running `easy_install nose` at a shell prompt.  To install PySnarl, download and unzip the source, then run `setup.py install` from the unzipped source's root directory.  Install snore the same way.  The source trees for PySnarl and snore may be deleted after installation.

Usage
=====

Running Nose with Snore
-----------------------

To enable Snarl notification of nose's test results via the snore plugin, simply add the `--with-snore` option to your `nosetests` command line.

Configuring Nose to Always Run with Snore
-----------------------------------------

nose can be configured to always use the snore plugin in two ways:

* Setting the environment variable `NOSE_WITH_SNORE` to 1 
* Placing `with-snore=1` in the `[nosetests]` section of the `.noserc` or `nose.cfg` file in your home directory

See the [nose usage documentation](http://somethingaboutorange.com/mrl/projects/nose/0.11.1/usage.html) for more info.

Customizing the Icons
---------------------

snore uses several icons to visually differentiate test results displayed via Snarl.  Three default icons are installed with the package:

* `error.png` is displayed when some tests found by nose have errors
* `fail.png` is displayed when some tests found by nose fail
* `pass.png` is displayed when all tests found by nose pass

For this release, the icons are included within the snore package.  They may be customized by replacing them with new PNG files of the same name.  The icons are found below your Python installation's `site-packages` directory.  For Windows machines, this directory is usually:  

    <python-install-directory>\Lib\site-packages\snore-X.X-pyY.Y.egg\snore\icons

The default icons are 200x200 pixel PNG images with transparent backgrounds.

Tests
=====

Unit tests are provided with the source distribution in the `test` directory.  These tests are intended to be run with `nosetests`.  There is currently no way to run the tests directly from the command line by executing the test scripts.  The tests should work whether or not the package has been installed.

Uninstallation
==============

Should you wish to remove snore, simply:

* Change to your Python installation's `site-packages` directory
* Remove the directory `snore-X.X-pyY.Y.egg` and its contents from the `site-packages` directory
* Remove the line referring to snore from the `easy-install.pth` file found in the `site-packages` directory

Author
======

Jon Speicher ([jon.speicher@gmail.com](mailto:jon.speicher@gmail.com))

Credits
=======

snore is pretty dumb.  For the most part, it just ties together existing software, and so credit is due to the authors of Snarl, PySnarl, and nose.  Additionally, I spent a good chunk of time studying [NoseGrowl](http://www.assembla.com/wiki/show/nosegrowl) as an example.

The [pass](http://commons.wikimedia.org/wiki/File:Support-filled.svg) and [fail](http://commons.wikimedia.org/wiki/File:Oppose-filled.svg) icons are public domain and were made by Wikimedia Commons user [Kalan](http://commons.wikimedia.org/wiki/User:Kalan).

License
=======

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