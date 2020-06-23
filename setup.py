#!/usr/bin/env python

from distutils.core import setup
setup(name='sergey',
      version='0.1',
      license='GPL 3.0',
      description='SERGEY: Slideshow software based on pygame',
      long_description='''
SERGEY

Slideshow software based on pygame. Includes titles (intertitles or
over top of pictures), panning along panoramic shots, zooming into (or
out of) higher-resolution shots, music, music titles with CD art.

Simple to use if you know Python. Currently will be somewhat confusing
if you don't, as all "slides" (or titles) are specified using Python.
      ''',
      author='Mike Warren',
      author_email='mike@mike-warren.com',
      url='http://www.mike-warren.com/sergey',
      
      py_modules=['sergey'],
      scripts=['sergey-ensure-resolution.py', 'sergey-from-dir.py']
      )
