#!/usr/bin/env python

from distutils.core import setup
setup(name='photoviewer',
      version='0.1',
      license='GPL 3.0',
      description='Picture viewer software based on pygame',
      long_description='''
      ''',
      author='Slippy',
      author_email='sidsnake@hotmail.co.uk',
      url='http://www.foo.co.uk',
      
      py_modules=['pv2'],
     #ß scripts=['','']
      entry_points='''
          [console_scripts]
          pv2=pv2:main
      '''
      )
