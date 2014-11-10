=================================================
                       bcut
=================================================
-------------------------------------------------
              Improved cut utitity
-------------------------------------------------

Description
===========

bcut is a improved version of the cut unix utility implemented in python3.2.
It improves upon the original by adding it ability to count bytes, characters
or fields from the end of the line.

Consider following example

:: 

    pkg-name-VERSION-patch
    longer-pkg-name-VERSION-patch
    very-very-long-pkg-name-VERSION-patch

How can you remove the last 2 fields from each line? With cut you can't, since
it always counts the fields from the start of the line. bcut aims to improve 
upon that.

I've decided to implement it in python since it looked like a nice exercise in
python programming.

Features
========

* All the features of coreutils cut utility
* Counting of fields from the end.

Installation
============

Dependencies
------------

* >= Python 3.2

Install
-------

Build and install by running:

    $ python setup.py build
    $ sudo python setup.py install

Usage
=====

::

    usage: bcut [-h] (-b LIST | -c LIST | -f LIST) [-d DELIM] [-n] [--complement]
                [-i] [-s] [--output-delimiter STRING] [--version]
                [files [files ...]]

    Print selected parts of lines from each FILE to standard output.

    positional arguments:
    files                 List of input FILEs to be processed. If none are
                          specified the input will be taken from stdin

    optional arguments:
    -h, --help            show this help message and exit
    -b, --bytes LIST      display only these bytes
    -c, --characters LIST display only these characters
    -f, --fields LIST     select only these fields; also print any line that
                          contains no delimiter character, unless the -s option
                          is specified
    -d, --delimiter DELIM use DELIM instead of TAB for field delimiter
    -n                    Do not split multi-byte characters (no-op for now).
    --complement          Complement the set of selected bytes, characters or
                          fields
    -i, --invert          Count butes, characters or fields from the end of the
                          line
    -s, --only-delimited  do not print lines not containing delimiters
    --output-delimiter STRING
                          use STRING as the output delimiter. The default is to
                          use the inpt delimiter
    --version             show program's version number and exit

    Use one, and only one of -b, -c or -f.  Each LIST is made up of one
    range, or many ranges separated by commas.  Selected input is written
    in the same order that it is read, and is written exactly once.
    Each range is one of:

     N     N'th byte, character or field, counted from 1
     N-    from N'th byte, character or field, to end of line
     N-M   from N'th to M'th (included) byte, character or field
     -M    from first to M'th (included) byte, character or field

    With no FILE, or when FILE is -, read standard input.

Download
========

See Releases_ page for all downloads.

Authors
=======

* Pawel 'l0ner' Soltys <pwslts@gmail.com>

License
=======

GNU GPLv3

Copyright (C) 2014 Pawel 'l0ner' Soltys <pwslts@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


:: _Releases: https://github.com/l0ner/bcut/releases/
