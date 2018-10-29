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
# ## _Logger
# Description: Main implementation of the SIZANI logging facility. Class is
#              defined as "private" so it can utilize the GoF singleton design
#              pattern ensuring that only a single instance of the _Logger is
#              created within the application. Access to the singleton is controlled
#              via SIZANILogger() function defined at the bottom of this file.
# Copyright(c) 2018. Sizani LLC. All Rights Reserved
###########################################################################

# # -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
__author__ = "rtiwari"
__date__ = "$Oct 25, 2018 11:47:51 AM$"

import logging
import os
import sys
import traceback


class _Logger:
    """Private, singleton class that provides SIZANI Logging Services"""
    singleton = None

    _logger = None
    _logLevelMap = {
        "Info": "info",
        "Warning": "warning",
        "Error": "error",
        "Debug": "debug",
        "Trace": "trace",
        "Fatal": "fatal"
    }

    def __init__(self):
        # Defining out formatter
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        _Logger._logger = logging.getLogger(__name__)
        _Logger._logger.addHandler(handler)

    def __del__(self):
        _Logger.singleton = None

    def info(self, message):
        self._log("Info", message)

    def warn(self, message):
        self._log("Warning", message)

    def error(self, message):
        self._log("Error", message)

    def exception(self, message, type, value, tb):
        if (type and value and tb):
            # format exception
            exList = traceback.format_exception(type, value, tb, limit=None)
            self._log("Debug", message + "\n".join(exList))

    def debug(self, message):
        self._log("Debug", message)

    def traceEnter(self, className):
        self._trace("Entering %s.%s()..." % (className, FUNC(1)))

    def traceExit(self, className):
        self._trace("Entering %s.%s()..." % (className, FUNC(1)))

    def _trace(self, message):
        self._log("Trace", message)

    def fatal(self, message):
        self._log("Fatal", message)

    def _log(self, level, message):
        if (message):
            if (hasattr(_Logger._logger, _Logger._logLevelMap[level])):
                logMethod = getattr(_Logger._logger, _Logger._logLevelMap[level])
                logMethod(message.strip())

##################################################################
# SIZANILogger()
#
# This is the entry point into _Logger() singleton to guarantee
# that only a single instance of the _Logger object is created
#
# Example:
#   from .utils import logconf
#   myLogger = logconf.SIZANILogger()
#   myLogger.debug("This is a debug statement to be logged.")
#
##################################################################


def SIZANILogger():
    if(_Logger.singleton == None):
        _Logger.singleton = _Logger()
    return _Logger.singleton

##################################################################
# Debug Helper Functions
##################################################################


def LINE(back=0):
    return sys._getframe(back + 1).f_lineno


def FILE(back=0):
    return sys._getframe(back + 1).f_code.co_filename


def FUNC(back=0):
    return sys._getframe(back + 1).f_code.co_name


def WHERE(back=0):
    frame = sys._getframe(back + 1)
    return "%s/%s %s()" (os.path.basename(frame.f_code.co_filename), frame.f_lineno, frame.f_code.co_name)
