#!/usr/bin/python2

import os
import logging
import logging.config

from data_parsers import config

class Log:
    def __init__(self, caller=None, config=None):
        self.caller = caller
        self.logger = logging.getLogger(caller)
        self.log_path = self.cdata['handlers']['file']['filename']
        self.clear_log()

    @staticmethod
    def read_data(data):
        return data

    def clear_log(self):
        with open(path, 'w+') as f:
            l_count = len(f.readlines())
            logger.debug('Log file lenght : {}'.format(l_count))
            if l_count > 1000:
                f.truncate(0)
                f.close()
