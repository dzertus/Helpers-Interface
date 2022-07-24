#!/usr/bin/env python3
import os

import logging
import logging.config


from utils import config_utils

CONFIG_RELATIVE_PATH = 'python/log/log.yaml'
LOG_RELATIVE_PATH = 'python/log/log.log'

def run_logger():
    # init logger
    config = config_utils.load_yaml(CONFIG_RELATIVE_PATH)
    logging.config.dictConfig(config)
    global logger
    logger = logging.getLogger('baseLogger')
    clear_log(LOG_RELATIVE_PATH)

def clear_log(path):
    with open(path, 'w+') as f:
        l_count = len(f.readlines())
        logger.debug('Log file lenght : {}'.format(l_count))
        if l_count > 1000:
            f.truncate(0)
            f.close()
