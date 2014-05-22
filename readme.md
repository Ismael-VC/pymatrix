
Pymatrix
========

A pure-Python matrix module with support for basic linear algebra operations.

Sample syntax:

    from pymatrix import matrix

    m = matrix([
        [1, 2],
        [3, 4]
    ])

    a = m + m * 2
    b = m * m
    c = m ** 3

    d = m.det()
    e = m.inverse()


Installation
------------

Install directly from the Python Package Index using `pip`:

    $ pip install pymatrix

Alternatively, download the source and run:

    $ python setup.py install


Requirements
------------

Tested with Python 2.7 and 3.2.


License
-------

This work has been placed in the public domain.
