try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

    config = {
            'description': 'bcut - Print selected parts of lines',
            'author': 'Pawel <l0ner> Soltys',
            'url': 'http://github.com/l0ner/bcut',
            'author_email': 'pwslts@gmail.com',
            'version': '0.1',
            'install_requires': [],
            'packages': ['bcut'],
            'scripts': [],
            'name': 'bcut'
            }

    setup(**config)
