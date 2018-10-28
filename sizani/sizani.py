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
#
# ## Main
# Description:
#
# Revision History:
#
# Date                  Author              Revision(s)
# -------------         ------------        ---------------
# Aug 30, 2018          rtiwari             Created initial version of the module
#
# Copyright(c) 2018. Sizani LLC. All Rights Reserved
###########################################################################
# # -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
__author__ = "rtiwari"
__date__ = "$Oct 25, 2018 11:47:51 AM$"

import sys
from . import murid
from sizani.lib.sizani.utils import args
from sizani.lib.sizani.utils import logconf


class SIZANI:
    _log = logconf.SIZANILogger()

    def __init__(self):
        try:
            self._log.traceEnter(self.__class__.__name__)
            # instantiate MURID container
            mm = murid.MURID()
            mm.monitor()
        finally:
            self._log.traceExit(self.__class__.__name__)


def main():
    ss = SIZANI()


if __name__ == '__main__':
    main()
