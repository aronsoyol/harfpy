#+
# Distutils script to install HarfPy. Invoke from the command line
# in this directory as follows:
#
#     python3 setup.py install
#
# Written by Lawrence D'Oliveiro <ldo@geek-central.gen.nz>.
#-

from setuptools import setup


setup(
    name = "HarfPy",
    version = "0.82",
    description = "language bindings for HarfBuzz",
    long_description =
        "language bindings for the HarfBuzz shaper library, for Python 3.3 or later",
    author = "Lawrence D'Oliveiro",
    author_email = "ldo@geek-central.gen.nz",
    url="https://github.com/aronsoyol/harfpy",
    license = "LGPL v2.1+",
    test_suite='test',
    py_modules = ["harfbuzz"]
)
