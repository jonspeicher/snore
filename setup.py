"""This script installs snore as a nose plugin."""

# Copyright (c) 2010 Jonathan Speicher (jon.speicher@gmail.com)
# Licensed under the MIT license: http://creativecommons.org/licenses/MIT

try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name = 'snore',
    version = '0.1',
    author = 'Jon Speicher',
    author_email = 'jon.speicher@gmail.com',
    description = 'A Snarl plugin for nose',
    url = "http://github.com/jonspeicher/snore",
    license = 'MIT',
    install_requires = ['nose>=0.11.1'],
    zip_safe = False,
    packages = ['snore'],
    package_data = { 'snore': ['icons/*.png'] },
    entry_points = { 'nose.plugins': ['snore = snore.builder:build'] }
    )