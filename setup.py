####################################################################
#
# bcut - a better cut utility
#
# Copyright (C) 2014 Pawel 'l0ner' Soltys <pwslts@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##########################################################################

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'bcut',
    'packages': ['bcut'],
    'version': '1.0',
    'description': 'bcut - Print selected parts of lines',
    'author': 'Pawel <l0ner> Soltys',
    'author_email': 'pwslts@gmail.com',
    'url': 'http://github.com/l0ner/bcut',
    'license': 'GNU GPLv3',
    'keywords': ['utility', 'cut'],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.2",
        "Development Status :: 5 - Production/Stable", 
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
        "Topic :: Utilities"
        ],
    'long_description': """\
            Print selected parts of lines from each FILE to standard output.
            """,
    'entry_points': {
        'console_scripts': [
            'bcut=bcut.__main__:main',
        ],
    },
    'data_files': [ ('share/man/man1', [ ('man/bcut.1') ] ) ]
}

setup(**config)

