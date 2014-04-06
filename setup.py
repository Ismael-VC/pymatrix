#!/usr/bin/env python3
"""
Pymatrix: a lightweight matrix module in pure Python with support for 
basic linear algebra operations.

"""

import os
import re
import io

from distutils.core import setup


def load_meta(*path):
    filepath = os.path.join(os.path.dirname(__file__), *path)
    with io.open(filepath, encoding='utf-8') as mfile:
        pystr = mfile.read()
        regex = r'''^__([a-z]+)__ = "(.*)"'''
        return dict(re.findall(regex, pystr, flags=re.MULTILINE))


meta = load_meta('pymatrix.py')


short_description = (
    'A lightweight matrix object with support for '
    'basic linear algebra operations.'
)


long_description = """\
See the module's Github homepage (https://github.com/xpxqx/pymatrix) 
for further details.
"""


setup(
    name = 'pymatrix',
    version = meta['version'],
    url = 'https://github.com/xpxqx/pymatrix',
    license = 'Public Domain',
    author = 'xpxqx',
    author_email = 'xpxqx@outlook.com',
    description = short_description,
    long_description = long_description,
    py_modules = ['pymatrix'],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'License :: Public Domain',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)
