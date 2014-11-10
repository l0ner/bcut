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
            'bcut=bcut:main',
        ],
    }
}

setup(**config)
