#!/usr/bin/env python3

import os
from models import model_abstract

class Script(model_abstract.ScriptAbstract):
    def __init__(self, path):
        super().__init__(path)
        print('Install Print TOTO')
        self.path = path
        self.name = 'Print Toto'
        self.dcc = ['maya']
        self.icon = os.path.join(r"C:\Users\youss\Documents\GitHub\Maya-Helper-Interface\icons",
                                 '{0}.{1}'.format(self.module_name, 'png'))

    def get_name(self):
        return type(self)

    def get_dcc(self):
        return self.dcc

    def get_icon(self):
        return self.icon

    def get_doc(self):
        return 'This script prints toto'

    def run(self):
        """
        Script Main Function
        """
        print('Hello it is Toto')