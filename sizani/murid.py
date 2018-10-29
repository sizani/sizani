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
# ## Main
# Description: Murid is a main module of sizani. Murid is an arabic word which
#              means the commited one. This module is the technically the entry point
#              of the application.
# Copyright(c) 2018. Sizani LLC. All Rights Reserved
###########################################################################
# # -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
__author__ = "rtiwari"
__date__ = "$Oct 25, 2018 11:47:51 AM$"

import sys
from sizani.lib.sizani.cloud.aws import session as awssession
from sizani.lib.sizani.core import exceptions
from sizani.lib.sizani.utils import args
from sizani.lib.sizani.utils import decor as p
from sizani.lib.sizani.utils import logconf
from sizani.lib.sizani.utils import yamlmgr


class MURID:
    # Custom logger
    _log = logconf.SIZANILogger()

    def __init__(self, appendCmdLineArgs=None):
        """Default constructor"""
        try:
            self._log.traceEnter(self.__class__.__name__)
            self._sessionImpl = None
            self._cmdLineArgs = None
            self._parse = None
            self._yaml = None
            self.refresh(appendCmdLineArgs)
        finally:
            self._log.traceExit(self.__class__.__name__)

    def __del__(self):
        """Default destructor"""
        try:
            self._log.traceEnter(self.__class__.__name__)
            pass
        finally:
            self._log.traceExit(self.__class__.__name__)

    def refresh(self, appendCmdLineArgs=None):
        try:
            self._log.traceEnter(self.__class__.__name__)
            try:
                self._cmdLineArgs = args.CmdLineArgs
                self._parse = self._cmdLineArgs()
                self._parse = self._parse.parse_option()
                if(self._parse.murid):
                    self._yaml = yamlmgr.YamlManager(self._parse.murid)
                else:
                    self._parse.print_help()
                    self._parse.exit()
                cloudprovider = self._yaml.getCloudProvider()
                if (cloudprovider == self._yaml.PROP_KEY_CLOUDPROVIDER_AWS):
                    self._sessionImpl = awssession.AWSSessionImpl(self._yaml)
                else:
                    self._log.error(
                        "Unsupported cloud provider value: %s. It needs to be in following format \n --- \n aws: \n\t aws_access_key_id: ACCESSKEYID \n\t aws_secret_access_key: SECRETACCESSKEY \n\t region: \n\t attributes:" % (cloudprovider))
            except:
                type, value, tb = sys.exc_info()
                self._log.exception("", type, value, tb)
                raise
        finally:
            self._log.traceExit(self.__class__.__name__)

    def getCmdLineArgs(self):
        try:
            self._log.traceEnter(self.__class__.__name__)
            return self._cmdLineArgs
        finally:
            self._log.traceExit(self.__class__.__name__)

    def monitor(self):
        try:
            self._log.traceEnter(self.__class__.__name__)
            try:
                if(self._sessionImpl):
                    self._sessionImpl.monitor()
                else:
                    pass
            except:
                type, value, tb = sys.exc_info()
                self._log.exception("", type, value, tb)
                raise
        finally:
            self._log.traceExit(self.__class__.__name__)
