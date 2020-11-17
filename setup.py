try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Skeleton Project',
    'author': 'indecipherable',
    'url': 'github.com',
    'download_url': 'https://github.com/indecipherable/twisted_smoke',
    'author_email': 'bluemage@no-data.org',
    'version': '0.1',
    'install_requires': ['python-nose'],
    'packages': [''],           # refactor
    'scripts': ['NA'],
    'name': 'twisted_smoke'
}

setup(**config)
