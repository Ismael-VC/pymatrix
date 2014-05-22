
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


Disclaimer
----------

I built this module for my own edutainment while taking an undergrad course in linear algebra. It's easy to use and ideal for verifying pen-and-paper calculations, but if you have serious number crunching to do, the math professors over at [numpy](http://www.numpy.org/) have a better solution for you.


License
-------

This work has been placed in the public domain.
