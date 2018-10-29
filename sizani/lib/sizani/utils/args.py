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
############################################################################
# ## CmdLineArgs
# Description: CmdLineArgs is a simple command line parser module of sizani.
#              This module is uses argparser module to parse the command line
#              arguments.
# Copyright(c) 2018. Sizani LLC. All Rights Reserved
###########################################################################
# # -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
__author__ = "rtiwari"
__date__ = "$Aug 30, 2018 11:47:51 AM$"

import argparse
from argparse_color_formatter import ColorHelpFormatter
import sys
from sizani.lib.sizani.utils import logconf
from sizani.__version__ import __version__


class CmdLineArgs:
    _log = logconf.SIZANILogger()

    def __init__(self):
        try:
            self._log.traceEnter(self.__class__.__name__)
            pass
        finally:
            self._log.traceExit(self.__class__.__name__)

    def __del__(self):
        try:
            self._log.traceEnter(self.__class__.__name__)
            pass
        finally:
            self._log.traceExit(self.__class__.__name__)

    def parse_option(self):
        parser = argparse.ArgumentParser(formatter_class=CustomFormatter,)
        parser.add_argument("-V", "--version", action="version",
                            version="%(prog)s {}".format(__version__))
        parser.add_argument("-f", "--file", dest="murid",
                            help="specify a murid file to run", metavar="FILE")
        if len(sys.argv[1:]) == 0:
            parser.print_help()
            parser.exit()
        return parser.parse_args(args=None, namespace=None)


class CustomFormatter(argparse.RawDescriptionHelpFormatter, ColorHelpFormatter):
    pass
