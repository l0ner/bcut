from distutils.core import setup

config = {
    'name': 'bcut',
    'packages': ['bcut'],
    'version': '0.1',
    'description': 'bcut - Print selected parts of lines',
    'author': 'Pawel <l0ner> Soltys',
    'author_email': 'pwslts@gmail.com',
    'url': 'http://github.com/l0ner/bcut',
    'keywords': [],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
        "Topic :: Utilities"
        ],
    'long_description': """\""",
    'install_requires': [],
    'scripts': [],
    }

setup(**config)
