# Copyright (2016) Alok Parlikar <alok@parlikar.com>

from distutils.core import setup, Extension

import os
print os.environ['FLITE_LIBS']
print os.environ['FLITE_INC']

inc_dirs=['flite/include']
lib_dirs=['flite/build/x86_64-linux-gnu/lib']

if os.environ['FLITE_INC']:
    inc_dirs = [os.environ['FLITE_INC'],]
if os.environ['FLITE_LIBS']:
    lib_dirs = [os.environ['FLITE_LIBS'],]


setup(name='pyflite',
      version='0.1',
      ext_modules=[Extension('_pyflite', ['pyflite.i', 'pyflite.c'],
                             include_dirs=inc_dirs,
                             library_dirs=lib_dirs,
                             libraries=['flite_cmulex', 'flite_usenglish', 'flite'],
                             swig_opts=['-modern', '-Iflite/include'])],
      py_modules=['pyflite']
)
