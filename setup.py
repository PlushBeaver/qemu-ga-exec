#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qemu_ga_exec",
    version="0.1",
    scripts=["qemu-ga-exec"],
    author="Dmitry Kozlyuk",
    author_email="dmitry.kozliuk@gmail.com",
    description="Command executor for QEMU Windows guests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PlushBeaver/qemu-ga-exec",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
)
