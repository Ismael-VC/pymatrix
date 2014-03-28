"""
Pymatrix: a lightweight matrix module in pure Python with support for 
basic linear algebra operations.

"""

from distutils.core import setup

short_description = (
    'A lightweight matrix object with support for '
    'basic linear algebra operations'
)

long_description = """\
See the module's Github homepage (https://github.com/xpxqx/pymatrix) 
for further details.
"""

setup(
    name = 'pymatrix',
    version = '0.5.0',
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
