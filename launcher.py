#!/usr/bin/env python3

#exec(open(r"C:\Users\youss\Documents\GitHub\Maya-Helper-Interface\launcher.py").read())
import sys
import os
import logging
#TODO Python 2/3
import importlib.util

from PySide2 import QtWidgets

# Adding MHI PYTHONPATH
MHI_PYTHONPATH = os.environ.get('MHI_PYTHONPATH')
if not MHI_PYTHONPATH in sys.path:
    sys.path.insert(0, MHI_PYTHONPATH)

from models.model_abstract import ScriptModel, ScriptAbstract
from controllers.classes import ClassicController
from data_parsers.path_parser import PathParser
from views import view_abstract


# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

###### PARSING SCRIPTS TO USE ######
#TODO : Put all in parser
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
        #TODO Python 2/3
        module_path = os.path.join(module_root, file)
        spec = importlib.util.spec_from_file_location(file, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        script = module.Script(module_root, file)
        scripts.append(script)

def main():


    logger.info('...Init App')

    current_app = ''
    print('Initializing Model')
    model = ScriptModel()
    print('Model Initialized')

    print('Initializing GUI')
    # print(sys.executable)
    app = QtWidgets.QApplication(sys.argv)
    view = view_abstract.NormalInterface()
    print('GUI Initialized')

    print('Initializing Controller')
    controller = ClassicController(model, view)
    print('Controller Initialized')
    controller.run_ui()
    print('Ui ready')


    for script in scripts:
        controller.add_item(script)

    sys.exit(app.exec_())
    logger.info('Running...')
if __name__ == '__main__':
    main()

