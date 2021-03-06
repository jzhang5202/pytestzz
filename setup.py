#coding:utf-8

import os
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

readme_file = os.path.join(here, 'README.md')

def read_text(file_path):
    """
    fix the default operating system encoding is not utf8.
    """
    if sys.version_info.major < 3:
        with open(file_path) as f:
            return f.read()
    with open(file_path, encoding="utf8") as f:
        return f.read()

README = read_text(os.path.join(here, 'README.md'))

requires = [

]

test_requirements = [
]


setup(
    name='pytestzz',
    description='Pure-Python pytestzz',
    version='1.0.0',
    author='jzhang5202',
    author_email='yujuan99099@163.com',
    packages=find_packages(),
    include_package_data=True,
    long_description=README,
    url='git@github.com:jzhang5202/pytestzz.git',
    platforms='all platform',
    license='BSD',
)
