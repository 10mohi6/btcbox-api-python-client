# coding: utf-8
try:
    import setuptools
    from setuptools import setup, find_packages
except ImportError:
    print("Please install setuptools.")

import os
long_description = 'btcbox-client is a python client (sync/async) library for btcbox api.'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

setup(
    name  = 'btcbox-client',
    version = '0.1.0',
    description = 'btcbox-client is a python client (sync/async) library for btcbox api.',
    long_description = long_description,
    license = 'MIT',
    author = '10mohi6',
    author_email = '10.mohi.6.y@gmail.com',
    url = 'https://github.com/10mohi6/btcbox-api-python-client',
    keywords = 'btcbox',
    packages = find_packages(),
    install_requires = ['grequests'],
    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Programming Language :: Python :: 3.6',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License'
    ]
)