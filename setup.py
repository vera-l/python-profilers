#! /usr/bin/python
# coding: utf8

from setuptools import setup
import sys

PY2 = sys.version_info[0] == 2

setup(
    name='profilers',
    version='0.1',
    description='Function decorators with some profilers',
    long_description='Function decorators with some profilers',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='profiler',
    url='http://iamvera.com',
    author='Vera Lobacheva',
    author_email='vera@iamvera.com',
    license='MIT',
    packages=['profilers'],
    # problem with cpython on line_profiling builder for python 3.7
    install_requires=[
        'yappi',
        'memory_profiler',
        'pycallgraph',
        'six',
        'gprof2dot',
    ] + (['line_profiler'] if PY2 else []),
    include_package_data=False,
    zip_safe=False
)
