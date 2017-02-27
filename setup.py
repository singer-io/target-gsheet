#!/usr/bin/env python

from setuptools import setup

setup(name='target-gsheet',
      version='0.1.0',
      description='Singer.io target for writing data to Google Sheets',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      install_requires=[
          'jsonschema',
          'singer-python>=0.1.0',
          'google-api-python-client'
      ],
      entry_points='''
          [console_scripts]
          target-gsheet=target_gsheet:main
      ''',
)
