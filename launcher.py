#!/usr/bin/env python3

#exec(open(r"C:\Users\youss\Documents\GitHub\Maya-Helper-Interface\launcher.py").read())
import sys
import os
import logging
#Todo : Python 2/3
import importlib.util

from PySide2 import QtWidgets

# Get MHI_PYTHONPATH env variable , if not existing, sets it
MHI_PYTHONPATH = os.environ.get('MHI_PYTHONPATH')
if not MHI_PYTHONPATH in sys.path:
    sys.path.insert(0, MHI_PYTHONPATH)

from models.model_cls import ScriptModel, ScriptAbstract
from handlers.handler_cls import Handler
from data_parsers.path_parser import PathParser
from log import log_utils
from utils import config_utils

CONFIG_RELATIVE_PATH = 'config.yaml'

# Logger instance
log_utils.run_logger()
logger = logging.getLogger('launcher')

logger.debug('Parsing scripts data')



def run(scripts=None):
    logger.info('...Init App')

    model = ScriptModel()

    # application
    logger.info('Running on : {}'.format(sys.executable))
    current_app = ''
    app = QtWidgets.QApplication(sys.argv)

    # handler
    h = Handler(model)
    h.run()

    for s in scripts:
        h.add_item(s)
        logger.debug('"{}" script added'.format(s.name))

    logger.info('Running...')
    sys.exit(app.exec_())

def main():
    # Setup config
    config = config_utils.load_yaml(CONFIG_RELATIVE_PATH)
    parser = PathParser(config)

    # Add native source path
    native_source_path = os.path.join(MHI_PYTHONPATH, 'scripts')
    parser.add_source(native_source_path, CONFIG_RELATIVE_PATH)
    sources = parser.get_sources()

    scripts = []

    for src in sources:
        dir_data = parser.get_scripts_from_source(src)

    for script_name in dir_data.keys():
        module_path = os.path.join(dir_data[script_name]['dir'], dir_data[script_name]['module'])
        spec = importlib.util.spec_from_file_location(script_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        script = module.Script(src, dir_data[script_name])
        scripts.append(script)

    run(scripts)

if __name__ == '__main__':
    main()

