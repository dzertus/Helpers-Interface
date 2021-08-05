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
scripts = []
for module_path in modules_paths:
    scripts.append(model_abstract.Script(module_path))

for script in scripts:
    print (script.get_name())

model = model_abstract.ScriptModel()
view = view_abstract.ViewAbstract()
controller = controller_abstract.Controller(model, view)






