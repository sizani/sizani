# -*- coding: utf-8 -*-
import boto3
from sizani.lib.sizani.core import interfaces
from sizani.lib.sizani.utils import logconf


class MonitorManager:
    log = logconf.SIZANILogger()

    def __init__(self, YamlManager):
        try:
            self.log.traceEnter(self.__class__.__name__)
            self._connected = 0
            self._yamlmgr = YamlManager
        finally:
            self.log.traceExit(self.__class__.__name__)

    def __del__(self):
        try:
            self.log.traceEnter(self.__class__.__name__)
            pass
        finally:
            self.log.traceExit(self.__class__.__name__)

    def connect(self):
        try:
            self._log.traceEnter(self.__class__.__name__)
            try:
                if(self._sessionImpl):
                    self._sessionImpl.connect()
                else:
                    pass
            except:
                type, value, tb = sys.exc_info()
                self._log.exception("", type, value, tb)
                raise
        finally:
            self._log.traceExit(self.__class__.__name__)
