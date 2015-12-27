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
        'Django==1.8.7',
        'Pillow==3.0.0',
        'pytz==2015.7',
        'django-mailgun==0.8.0',
        'django-dbbackup===2.3.2',
        'dropbox==4.0'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/',
        'https://pypi.python.org/simple/pillow/',
        'https://pypi.python.org/simple/pytz/',
        'https://pypi.python.org/simple/django-mailgun/',
        'https://pypi.python.org/django-dbbackup/',
        'https://pypi.python.org/dropbox/'
    ],
)
