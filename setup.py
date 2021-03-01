#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='photoviewer',
      version='0.2',
      license='GPL 3.0',
      description='Picture viewer software based on pygame',
      long_description='''
      ''',
      author='Slippy',
      author_email='sidsnake@hotmail.co.uk',
      url='http://www.foo.co.uk',

      packages=find_packages(
            ),
      # package_dir = {"":"src"},
      # py_modules=["six"],

      install_requires=[
            'pillow==8.0.1',
            'pygame>=2.0.0',
            'requests==2.25.1',
            'sqlalchemy==1.3.22',
      ],
      
      scripts = ['bin/photoviewer'],

      # entry_points={
      #       'console_scripts': ['photoviewer=photoviewer.photoviewer:main']
      # },
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',

      )
