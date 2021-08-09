#!/usr/bin/env python3

import os
from models import model_abstract

class Script(model_abstract.ScriptAbstract):
    def __init__(self, path):
        super().__init__(path)
        self.path = path
        self.name = 'Print Toto 2'
        self.dcc = ['maya']
        self.icon = os.path.join(r"C:\Users\youss\Documents\GitHub\Maya-Helper-Interface\icons",
                                 '{0}.{1}'.format(self.module_name, 'png'))

    def run(self):
      print('Print Toto 2')

    def get_name(self):
        return type(self)

    def get_dcc(self):
        return self.dcc

    def get_icon(self):
        return self.icon
