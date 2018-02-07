from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name = 'fo-crawler',
    version = '0.1.1.4',
    keywords = ('cctv', 'crawler', 'focus on'),
    description = 'Crawler to fetch focus on(CCTV)',
    license = 'GPLv3',

    author = 'Johann Lee',
    author_email = 'me@qinka.pro',

    packages = find_packages(),
)
