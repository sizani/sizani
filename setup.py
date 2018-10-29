#
# Author:: Ravi Tiwari (rtiwariops@gmail.com)
# Copyright:: Copyright 2018, SIZANI Inc.
# License:: Apache License, Version 2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# # -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

import glob
import io
import os.path
import setuptools
import sys

MODULE_NAME = "sizani"
REPOSITORY_URL = "https://github.com/sizani/{:s}".format(MODULE_NAME)
REQUIREMENT_DIR = "requirements"
ENCODING = "utf8"

pkg_info = {}

setuptools_require = ["setuptools>=38.3.0"]

with open(os.path.join(MODULE_NAME, "__version__.py")) as f:
    exec(f.read(), pkg_info)

with io.open("README.md", encoding=ENCODING) as fp:
    long_description = fp.read()

with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

setuptools.setup(
    name=MODULE_NAME,
    version=pkg_info["__version__"],
    author=pkg_info["__author__"],
    author_email=pkg_info["__email__"],
    license=pkg_info["__license__"],
    packages=setuptools.find_packages(exclude=["test*"]),
    zip_safe=False,
    include_package_data=True,
    keywords=["aws", "cloud", "ec2"],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    install_requires=setuptools_require + install_requires,
    setup_requires=setuptools_require,
    extras_require={
        "build": ["wheel"],
        "release": ["releasecmd>=0.0.2"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    scripts=[
        MODULE_NAME + '/bin/sizani',
    ],
    entry_points={
        "console_scripts": [
            "sizani=sizani.sizani:main",
        ],
    }
)
