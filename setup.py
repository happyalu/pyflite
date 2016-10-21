# Copyright (2016) Alok Parlikar <alok@parlikar.com>

from distutils.core import setup, Extension

setup(name='pyflite',
      version='0.1',
      ext_modules=[Extension('_pyflite', ['pyflite.i', 'pyflite.c'],
                             include_dirs=['flite/include'],
                             library_dirs=['flite/build/x86_64-linux-gnu/lib'],
                             libraries=['flite_cmulex', 'flite_usenglish', 'flite'],
                             swig_opts=['-modern', '-Iflite/include'])],
      py_modules=['pyflite']
)
