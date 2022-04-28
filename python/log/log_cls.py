#!/usr/bin/env python3
import os

import logging
import logging.config

import yaml
from yaml.loader import SafeLoader

def run_logger():
    # init logger
    config = load_config('python/log/log.yaml')
    logging.config.dictConfig(config)
    global logger
    logger = logging.getLogger('baseLogger')
    clear_log('python/log/log.log')

def load_config(path):
    with open(path) as f:
        data = yaml.load(f, Loader=SafeLoader)
        f.close()
        return data

def clear_log(path):
    with open(path, 'w+') as f:
        l_count = len(f.readlines())
        logger.debug('Log file lenght : {}'.format(l_count))
        if l_count > 1000:
            f.truncate(0)
            f.close()