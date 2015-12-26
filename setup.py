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
        'Django<1.9',
        'Pillow',
        'pytz',
        'django-mailgun',
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/',
        'https://pypi.python.org/simple/pillow/',
        'https://pypi.python.org/simple/pytz/',
        'https://pypi.python.org/simple/django-mailgun/',
    ],
)
