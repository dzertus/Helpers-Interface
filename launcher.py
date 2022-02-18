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
