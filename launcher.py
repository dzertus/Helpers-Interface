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
from log import log_cls

# Logger instance
log_cls.run_logger()


logger = logging.getLogger('launcher')

logger.debug('Parsing scripts data')
#Todo : Move to parser
parser = PathParser()

native_source_path = os.path.join(MHI_PYTHONPATH, 'scripts')
src_paths = [native_source_path]

scripts = []
for src_path in src_paths:
    parser.new_root(src_path)
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

    model = ScriptModel()

    # application
    print(sys.executable)
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

if __name__ == '__main__':
    main()

