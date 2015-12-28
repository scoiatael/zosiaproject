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
        'Pillow==2.9.0',
        'pytz==2015.4',
        'django-mailgun==0.3.0',
        'django-dbbackup==2.3.3',
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/',
        'https://pypi.python.org/simple/django-mailgun/',
        'https://pypi.python.org/simple/django-dbbackup/',
    ],
)
