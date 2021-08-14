import sys
import os
import importlib.util

from models.model_abstract import ScriptModel, ScriptAbstract
from controllers.classes import ClassicController

from environment import Env
from data_parsers.path_parser import PathParser

###### ENVIRONMENT VARIABLES SETTING ######
env = Env()
env.add_path_variable(name='MHI_PYTHON_PATH', path=r'C:\Users\youss\Documents\GitHub\Maya-Helper-Interface\python')
MHI_PYTHON_PATH = os.environ.get('MHI_PYTHON_PATH')

###### PARSING SCRIPTS TO USE ######
#TODO : Put all in parser
parser = PathParser(None)

native_source_path = os.path.join(MHI_PYTHON_PATH, 'scripts')
source_paths = list()
source_paths.append(native_source_path)

modules_paths = []
for source_path in source_paths:
    parser.new_path(source_path)
    modules_paths.extend(parser.get_modules())

scripts = []
for module_path in modules_paths:
    script = ScriptAbstract(module_path)
    module_name = script.get_module_name()
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    script = module.Script(module_path)
    scripts.append(script)


###### MAIN  ######
def main():
    # Initialize Model
    model = ScriptModel()

    # Initialize View/GUI
    view = None

    # Initialize Controller
    controller = ClassicController(model, view)

    for script in scripts:
        module_name = script.get_module_name()
        module_path = script.get_module_path()
        controller.add_item(script)

    sys.exit(controller.app.exec_())


main()
