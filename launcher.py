#exec(open(r"C:\Users\youss\Documents\GitHub\Maya-Helper-Interface\launcher.py").read())
import sys
import os
#TODO Python 2/3
import importlib.util

# Adding MHI PYTHONPATH
MHI_PYTHONPATH = os.environ.get('MHI_PYTHONPATH')
if not MHI_PYTHONPATH in sys.path:
    sys.path.insert(0, MHI_PYTHONPATH)

from models.model_abstract import ScriptModel, ScriptAbstract
from controllers.classes import ClassicController
from data_parsers.path_parser import PathParser

###### PARSING SCRIPTS TO USE ######
#TODO : Put all in parser
parser = PathParser(None)

native_source_path = os.path.join(MHI_PYTHONPATH, 'scripts')
source_paths = list()
source_paths.append(native_source_path)

scripts = []
for source_path in source_paths:
    parser.new_path(source_path)
    modules = parser.get_modules()
    for module_name in modules:
        script = ScriptAbstract(source_path, module_name)
        module_name = script.module_name#.replace('.py', '')
        module_path = script.module_path
        print('Module Name : ', module_name)
        print('Module Path : ', module_path)

        #TODO Python 2/3
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        scripts.append(script)


###### MAIN  ######
def main():
    current_app = ''
    # Initialize Model
    model = ScriptModel()
    print('Model Initialized')

    # Initialize View/GUI
    view = None

    # Initialize Controller
    controller = ClassicController(model, view)

    for script in scripts:
        #print(sys.executable)
        controller.add_item(script)

    sys.exit(controller.app.exec_())


main()
