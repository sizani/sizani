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
from __future__ import absolute_import, print_function


class SIZANIException(Exception):
    """Base SIZANI exception class. All SIZANI exceptions extend this class"""

    def __init__(self, value):
        self.value = value

    def __del__(self):
        pass

    def __str__(self):
        return repr(self.value)


class MethodNotImplementedException(SIZANIException):
    """Exception thrown to indicate that an "abstract" method defined in
       a super class is not implemented by a sub class"""

    def __init__(self, value):
        SIZANIException.__init__(self, value)

    def __del__(self):
        SIZANIException.__del__()

    def __str__(self):
        return repr(self.value)


class MandatoryAttributeException(SIZANIException):
    """Exception thrown when a mandatory attribute value is not provided
       for a particular operation"""

    def __init__(self, value):
        SIZANIException.__init__(self, value)

    def __del__(self):
        SIZANIException.__del__()

    def __str__(self):
        return repr(self.value)
