#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2019, Juan B Cabral
# License: BSD-3-Clause
#   Full Text: https://github.com/leliel12/pert/blob/master/LICENSE


# =============================================================================
# DOCS
# =============================================================================

"""This file is for distribute pert

"""


# =============================================================================
# IMPORTS
# =============================================================================

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages  # noqa


# =============================================================================
# CONSTANTS
# =============================================================================

REQUIREMENTS = ["numpy"]


with open("README.md") as fp:
    LONG_DESCRIPTION = fp.read()


DESCRIPTION = LONG_DESCRIPTION.splitlines()[2]


# =============================================================================
# FUNCTIONS
# =============================================================================

def do_setup():
    setup(
        name="pert",
        version="2019.11",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        author="Juan BC",
        author_email="jbc.develop@gmail.com",
        url="https://github.com/leliel12/pert",
        license="3 Clause BSD",
        keywords=["pert", "project", "review", "statistics"],
        classifiers=(
            "Development Status :: 4 - Beta",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Scientific/Engineering"),
        py_modules=["pert", "ez_setup"],
        install_requires=REQUIREMENTS)


if __name__ == "__main__":
    do_setup()
