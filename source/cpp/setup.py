"""
⚙️ Cython Build Script: Compile C++ Extension for Python

Purpose:
- Builds the Cython binding `solution.pyx` as a C++ extension
- Enables Python code to call the C++ Solution class
- Supports seamless testing of C++ implementations from Python

Usage:
- python setup.py build_ext --inplace

Notes:
- Keeps the build process minimal and explicit
- language_level=3 ensures Python 3 semantics
- Named extension 'solution' for consistency across imports
"""

from setuptools import setup, Extension
from Cython.Build import cythonize

ext = Extension(name = "solution", sources = ["solution.pyx"], language = "c++")
setup(ext_modules = cythonize(ext, language_level = 3))