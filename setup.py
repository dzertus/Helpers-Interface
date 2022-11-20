#!/usr/bin/python3

from setuptools import setup
setup(
    name='hi_helpers'
    version='1.0',
    author='Youssef Taktak',
    description='Desktop application ui where we can add differents tools/helpers',
    url='https://github.com/dzertus',
    python_requires='>2.7',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        'yaml',
        'PIL'
    ],
    package_data={
        'sample': ['sample_data.csv'],
    },
    entry_points={
        'runners': [
            'hihelpers=python:main',
        ]
    }
)