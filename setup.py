#!/usr/bin/env python

from setuptools import setup

setup(name='target-gsheet',
      version='0.2.2',
      description='Singer.io target for writing data to Google Sheets',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['target_gsheet'],
      install_requires=[
          'jsonschema==2.6.0',
          'singer-python==0.1.0',
          'google-api-python-client==1.6.2'
      ],
      entry_points='''
          [console_scripts]
          target-gsheet=target_gsheet:main
      ''',
)
