#!/usr/bin/python2

import os
import logging
import logging.config



HI_PYTHONPATH = os.environ['HI_PYTHONPATH']
CONFIG_PATH = os.path.join(HI_PYTHONPATH, 'log/log.yaml')
LOG_PATH = os.path.join(HI_PYTHONPATH, 'log/log.log')

def run_logger():
    # init logger
    config = config_utils.load_yaml(CONFIG_PATH)
    logging.config.dictConfig(config)
    global logger
    logger = logging.getLogger('baseLogger')
    clear_log(LOG_PATH)

def clear_log(path):
    with open(path, 'w+') as f:
        l_count = len(f.readlines())
        logger.debug('Log file lenght : {}'.format(l_count))
        if l_count > 1000:
            f.truncate(0)
            f.close()
