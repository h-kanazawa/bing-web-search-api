# -*- coding: utf-8 -*-

"""
Client for Bing API v5 Web Search

See API Reference:
https://msdn.microsoft.com/en-us/library/dn760794.aspx
"""

import os
import sys

from setuptools import find_packages, setup

sys.path.append('./bing_web_search_api')
sys.path.append('./tests')

PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(PACKAGE_ROOT, 'README.rst')) as file_obj:
    README = file_obj.read()

setup(
    name='bing-web-search-api',
    version='0.0.1',
    description='Client for Bing API v5 Web Search',
    long_description=README,
    url='https://github.com/h-kanazawa/bing-web-search-api',
    author='h-kanazawa',
    author_email='hotaka-kanazawa@dac.co.jp',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='bing',
    packages=find_packages(exclude=['tests']),
    install_requires=['httplib2'],
    test_suite='test_client.suite',
)
