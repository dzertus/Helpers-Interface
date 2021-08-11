#!/usr/bin/env python3

"""
Replace #TODO
"""

import os
from models import model_abstract

class Script(model_abstract.ScriptAbstract):
    def __init__(self, path):
        super().__init__(path)
        self.path = path
        self.name = 'Template Script' #TODO
        self.dcc = [None] #TODO
        self.icon = os.path.join(r"[PATH]", self.module_name) #TODO

    def get_name(self):
        """
        Returns Script NickName
        :return: (str)
        """
        return self.name

    def get_dcc(self):
        """
        Dcc support
        :return: (list(str))
        """
        return self.dcc

    def get_icon(self):
        """
        Icon Path
        :return: (str)
        """
        return self.icon

    def run(self):
        """
        Script Main Function
        """
        # TODO
        return None