import os
from collections import defaultdict

from models import model_abstract
from views import view_abstract
from controllers import controller_abstract
from data_parsers import parser_path, classes

source_path = r"C:\Users\youss\Documents\GitHub\Maya-Helper-Interface\scripts"

scripts = defaultdict(lambda: -1)

parser = parser_path.ParserPath(source_path)

modules_paths = parser.get_modules()
modules = []
for module_path in modules_paths:
    modules.append(classes.Module(module_path))
for module in modules:
    print (module.get_content())

model = model_abstract.ScriptModel()
view = view_abstract.ViewAbstract()
controller = controller_abstract.Controller(model, view)






