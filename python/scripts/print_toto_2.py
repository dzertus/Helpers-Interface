#!/usr/bin/env python3

from models import model_cls

class Script(model_cls.ScriptAbstract):
    def __init__(self, source_path, name):
        super().__init__(source_path, name)
        print('Install Print TOTO')
        self.name = 'Print Toto 2'
        self.dcc = ['maya']
        print('Icon : ', self.icon_path)

    def get_name(self):
        return type(self)

    def get_dcc(self):
        return self.dcc

    def get_icon(self):
        pass

    def get_doc(self):
        return 'This script prints toto'

    def run(self):
        """
        Script Main Function
        """
        print('Hello it is Toto 2')