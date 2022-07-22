#!/usr/bin/env python3

"""
Replace # Todo : Fill Todo list and rename the file
"""

import os
from models import model_cls


class Script(model_cls.ScriptAbstract):
    def __init__(self, path):
        super().__init__(path)
        self.path = path
        self.name = 'Template Script'  # Todo : Fill with name
        self.dcc = [None]  # Todo : Fill list , eg : [os, maya]
        self.icon = os.path.join(r"[PATH]", self.module_name)  # Todo : Replace [PATH] by path to icon

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
        return self.icon_path

    def run(self):
        """
        Script Main Function
        """
        # Todo : Fill with your script
        return None
