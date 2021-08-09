import importlib.util
import sys
from collections import defaultdict

from models import model_abstract
from views import view_abstract
from controllers import controller_abstract
from data_parsers import path_parser

from PySide2 import QtWidgets


source_paths = [r"C:\Users\youss\Documents\GitHub\Maya-Helper-Interface\python\scripts"]

parser = path_parser.PathParser(None)
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

model = model_abstract.ScriptModel()


app = QtWidgets.QApplication(sys.argv)
view = view_abstract.Interface()
view.show()
controller = controller_abstract.Controller(model, view)

for script in scripts:
    module_name = script.get_module_name()
    module_path = script.get_module_path()
    controller.add_item(script)

controller.show_items()

sys.exit( app.exec_() )