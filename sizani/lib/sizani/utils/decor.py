# # -*- coding: utf-8 -*-
import re
from sizani.lib.sizani.utils import logconf
from colorama import Fore, Style


class Decor:
    _log = logconf.SIZANILogger()

    def __init__(self, message=None):
        """Default constructor"""
        try:
            self._log.traceEnter(self.__class__.__name__)
            self._message = None
            regexp = re.compile("No EC2 instance found in given region")
            if regexp.search(message):
                self.prompt_print_warn(message)
            else:
                self.prompt_print_success(message)
        finally:
            self._log.traceExit(self.__class__.__name__)

    def __del__(self):
        """Default destructor"""
        try:
            self._log.traceEnter(self.__class__.__name__)
            pass
        finally:
            self._log.traceExit(self.__class__.__name__)

    def prompt_print_success(self, message):
        """ Simple prompt funtion to print success output. """
        self._message = message
        print(Fore.GREEN + Style.BRIGHT + self._message + Fore.RESET)

    def prompt_print_warn(self, message):
        """ Simple prompt funtion to print success output. """
        self._message = message
        print(Fore.YELLOW + Style.BRIGHT + self._message + Fore.RESET)
