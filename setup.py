#!/usr/bin/env python
"""
Flask-RouteLogger
-----------

Logs the meta route level information with minimal config for flask application

"""

from setuptools import setup

setup(
    name='Flask-RouteLogger',
    version='0.1',
    url='',
    license='BSD',
    author='Navaneethan Ramasamy',
    author_email='nava.nmr@gmail.com',
    description='Logs the meta route level information with minimal config in flask application',
    long_description=__doc__,
    packages=[
        'flask_routelogger',
    ],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
	'elasticsearch'
    ],
    test_suite='test_cache',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
