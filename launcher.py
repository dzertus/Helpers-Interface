import sys
import os
import importlib.util

from PySide2 import QtWidgets

from models import model_abstract
from views import view_abstract
from controllers import controller_abstract

from environment import Env
from data_parsers import path_parser

###### ENVIRONMENT VARIABLES SETTING ######
env = Env()
env.add_path_variable(name='MHI_PYTHON_PATH', path=r'C:\Users\youss\Documents\GitHub\Maya-Helper-Interface\python')
MHI_PYTHON_PATH = os.environ.get('MHI_PYTHON_PATH')

###### PARSING SCRIPTS TO USE ######
parser = path_parser.PathParser(None)

native_source_path = os.path.join(MHI_PYTHON_PATH, 'scripts')
source_paths = list()
source_paths.append(native_source_path)

modules_paths = []
for source_path in source_paths:
    parser.new_path(source_path)
    modules_paths.extend(parser.get_modules())

scripts = []
for module_path in modules_paths:
    script = model_abstract.ScriptAbstract(module_path)
    module_name = script.get_module_name()
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    script = module.Script(module_path)
    scripts.append(script)


###### MAIN  ######
def main():
    # Initialize Model
    model = model_abstract.ScriptModel()

    # Initialize View/GUI
    app = QtWidgets.QApplication(sys.argv)
    view = view_abstract.InterfaceController()

    # Initialize Controller
    controller = controller_abstract.Controller(model, view)


    for script in scripts:
        module_name = script.get_module_name()
        module_path = script.get_module_path()
        controller.add_item(script)

    controller.show_items()
    sys.exit(app.exec_())

main()