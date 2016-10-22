# Copyright (2016) Alok Parlikar <alok@parlikar.com>

from distutils.core import setup, Extension

import os

try:
    inc_dirs = [os.environ['FLITE_INC'],]
except KeyError:
    inc_dirs=['flite/include']

try:
    lib_dirs = [os.environ['FLITE_LIBS'],]
except KeyError:
    lib_dirs=['flite/build/x86_64-linux-gnu/lib']

setup(name='pyflite',
      version='0.1',
      ext_modules=[Extension('_pyflite', ['pyflite.i', 'pyflite.c'],
                             include_dirs=inc_dirs,
                             library_dirs=lib_dirs,
                             libraries=['flite_cmulex', 'flite_usenglish', 'flite'],
                             swig_opts=['-modern', '-Iflite/include'])],
      py_modules=['pyflite']
)
