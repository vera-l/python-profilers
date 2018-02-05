#! /usr/bin/python
# coding: utf8

from setuptools import setup

setup(
    name='profilers', 
    version='0.1', 
    description='Function decorators with some profilers', 
    long_description='Function decorators with some profilers', 
    classifiers=[ 
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 2.7', 
    ], 
    keywords='profiler', 
    url='http://iamvera.com', 
    author='Vera Lobacheva', 
    author_email='vera@iamvera.com', 
    license='MIT', 
    packages=['profilers'], 
    install_requires=[
        'yappi',
        'line_profiler',
        'memory_profiler',
        'pycallgraph'
    ],
    include_package_data=False, 
    zip_safe=False
)
