#!/usr/bin/python3

from setuptools import setup

setup(
    name='flask-mongo-test',
    packages=['server'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
