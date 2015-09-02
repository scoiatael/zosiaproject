#!/usr/bin/env python

from setuptools import setup

setup(
    name='zosiaproject',
    version='0.1',
    description='OpenShift App',
    author='KSI',
    author_email='zosia@cs.uni.wroc.pl',
    url='http://ksi.ii.uni.wroc.pl/',
    install_requires=[
        'Django==1.8.4',
        'Pillow==2.9.0'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
