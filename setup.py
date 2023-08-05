from setuptools   import setup
from Cython.Build import cythonize

cython_source_file = 'src/imppkg/harmonic_mean.pyx'

setup(ext_modules = cythonize(cython_source_file, language_level = 3))
