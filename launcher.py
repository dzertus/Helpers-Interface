#!/usr/bin/env python3

#exec(open(r"C:\Users\youss\Documents\GitHub\Maya-Helper-Interface\launcher.py").read())
import sys
import os
import logging
#Todo : Python 2/3
import importlib.util

from PySide2 import QtWidgets

# Adding MHI PYTHONPATH
MHI_PYTHONPATH = os.environ.get('MHI_PYTHONPATH')
if not MHI_PYTHONPATH in sys.path:
    sys.path.insert(0, MHI_PYTHONPATH)

from models.model_cls import ScriptModel, ScriptAbstract
from handlers.handler_cls import Handler
from data_parsers.path_parser import PathParser
from ui import view_cls
from log import log_cls

# Logger
log_cls.run_logger()
logger = logging.getLogger('baseLogger')


logger.debug('Parsing scripts data')
#Todo : Move to parser
parser = PathParser()

native_source_path = os.path.join(MHI_PYTHONPATH, 'scripts')
source_paths = [native_source_path]

scripts = []
for source_path in source_paths:
    parser.new_root(source_path)
    modules = parser.get_modules()
    module_root = modules['root']
    modules_files = modules['files']
    for file in modules_files:
        #Todo : Python 2/3
        module_path = os.path.join(module_root, file)
        spec = importlib.util.spec_from_file_location(file, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        script = module.Script(module_root, file)
        scripts.append(script)

def main():
    logger.info('...Init App')

    #Todo : Get current app to init app var
    current_app = ''
    logger.debug('Initializing Model')
    model = ScriptModel()
    logger.debug('Model Initialized')

    logger.debug('Initializing GUI')
    # print(sys.executable)
    app = QtWidgets.QApplication(sys.argv)
    view = view_cls.DefaultInterface()
    logger.debug('GUI Initialized')

    logger.debug('Initializing Controller')
    controller = Handler(model, view)
    logger.debug('Controller Initialized')
    controller.run_ui()
    logger.info('Ui ready')

    for script in scripts:
        controller.add_item(script)
        logger.debug('"{}" script added'.format(script.name))

    logger.info('Running...')
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

