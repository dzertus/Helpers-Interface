#!/usr/bin/env python3

import os

from collections import defaultdict

class Model():
    def __iter__(self):
        raise NotImplementedError

    def get(self, item):
        """Returns an object with a .items() call method
        that iterates over key,value pairs of its information."""
        raise NotImplementedError

    @property
    def item_type(self):
        raise NotImplementedError

class ScriptModel(Model):
    print('Initialize Model')
    item_type = "script"

    def __init__(self, scripts=None):
        if scripts is None:
            scripts = defaultdict(lambda: -1)
        self.scripts = scripts

    def __iter__(self):
        yield from self.scripts

    def add(self, script):
        """
        Append in Scripts
        :param product:
        :return:
        """
        self.scripts[script.name] = script

    def remove(self, script_name):
        """
        Pop from Scripts
        :param product_name:
        :return:
        """
        self.scripts.pop(script_name)

    def get(self, script):
        try:
            return self.scripts[script]
        except KeyError as e:
            raise KeyError(str(e) + " not in the model's item list.")

class ScriptAbstract():
    def __init__(self, path):
        self.path = path
        self.module_name = os.path.splitext(os.path.basename(self.path))[0]
        self.name = None
        self.dcc = None
        self.icon = None

    def run(self):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

    def get_dcc(self):
        raise NotImplementedError

    def get_icon(self):
        raise NotImplementedError

    def get_doc(self):
        pass
    def get_module_name(self):
        return self.module_name

    def get_module_path(self):
        return self.path
