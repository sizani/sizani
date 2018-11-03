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
import yaml
from sizani.lib.sizani.utils import logconf


class YamlManager:
    PROP_KEY_CLOUDPROVIDER_AWS = "aws"
    _log = logconf.SIZANILogger()

    def __init__(self, filename=None):
        try:
            self._log.traceEnter(self.__class__.__name__)
            self._filename = None
            self._data = None
            self._awscreds = {}
            if(filename):
                self._filename = filename
                self.loadFromFile(filename)
        finally:
            self._log.traceExit(self.__class__.__name__)

    def loadFromFile(self, filename):
        try:
            self._log.traceEnter(self.__class__.__name__)
            self._filename = filename
            self._load(self)
        finally:
            self._log.traceExit(self.__class__.__name__)

    def getFilename(self):
        try:
            self._log.traceEnter(self.__class__.__name__)
            return self._filename
        finally:
            self._log.traceExit(self.__class__.__name__)

    def refresh(self):
        try:
            self._log.traceEnter(self.__class__.__name__)
            self._load(self, 1)
        finally:
            self._log.traceExit(self.__class__.__name__)

    def getCloudProvider(self):
        try:
            self._log.traceEnter(self.__class__.__name__)
            try:
                for provider in self._data:
                    if (provider):
                        provider = provider.lower()
                return provider
            except TypeError as te:
                self._log.error("Expected mandatory required values missing.")
            except AttributeError as ae:
                self._log.error("Expected mandatory required value is case sensitive.")
        finally:
            self._log.traceExit(self.__class__.__name__)

    def readYAML(self):
        try:
            self._log.traceEnter(self.__class__.__name__)
            try:
                self._awscreds['aws_access_key_id'] = self._data['aws']['aws_access_key_id']
                self._awscreds['aws_secret_access_key'] = self._data['aws']['aws_secret_access_key']
                self._awscreds['region'] = self._data['aws']['region']
                self._awscreds['resources'] = self._data['aws']['resources']
                self._awscreds['attributes'] = self._data['aws']['attributes']
                format = "format" in self._data['aws']
                if (format == True):
                    self._awscreds['format'] = self._data['aws']['format']
                else:
                    self._awscreds['format'] = 'table'
                monitoring = "monitoring" in self._data['aws']
                if(monitoring == True):
                    self._awscreds['monitoring'] = self._data['aws']['monitoring']
                else:
                    self._awscreds['monitoring'] = None
                ssh = "ssh" in self._data['aws']
                if(ssh == True):
                    self._awscreds['ssh'] = self._data['aws']['ssh']
                else:
                    self._awscreds['ssh'] = None
                auth_type = "auth_type" in self._data['aws']['ssh']
                if(auth_type == True):
                    self._awscreds['auth_type'] = self._data['aws']['ssh']['auth_type']
                else:
                    self._awscreds['auth_type'] = None
                username = "username" in self._data['aws']['ssh']
                if(username == True):
                    self._awscreds['username'] = self._data['aws']['ssh']['username']
                else:
                    self._awscreds['username'] = None
                access_key = "access_key" in self._data['aws']['ssh']
                if(access_key == True):
                    self._awscreds['access_key'] = self._data['aws']['ssh']['access_key']
                else:
                    self._awscreds['access_key'] = None
                password = "password" in self._data['aws']['ssh']
                if(password == True):
                    self._awscreds['password'] = self._data['aws']['ssh']['password']
                else:
                    self._awscreds['password'] = None
                return self._awscreds
            except (KeyError, TypeError) as kt:
                self._log.error(
                    "Missing mandatory value %s is missing in the murid yaml file which needs to be in following format \n aws_access_key_id: \n aws_secret_access_key: \n region: \n attributes: " % (kt))
            except:
                type, value, tb = sys.exc_info()
                self._log.exception("", type, value, tb)
                raise
        finally:
            self._log.traceExit(self.__class__.__name__)

    def _load(self, refresh=0):
        try:
            self._log.traceEnter(self.__class__.__name__)
            fis = None
            try:
                if(self._filename is None):
                    raise FileNotFoundError
                if(refresh == 1):
                    self.clear()
                fis = open(self._filename)
                self._data = yaml.load(fis)
            except IOError as fe:
                self._log.error(
                    "Missing yaml file: The file %s that is passed via command line does not exists" % (fis))
            except:
                self._close(fis)
            else:
                self._close(fis)
        finally:
            self._log.traceExit(self.__class__.__name__)

    def _close(self, fis):
        try:
            self._log.traceEnter(self.__class__.__name__)
            if(fis):
                try:
                    fis.close()
                except:
                    # don`t care on this exception
                    pass
        finally:
            self._log.traceExit(self.__class__.__name__)
