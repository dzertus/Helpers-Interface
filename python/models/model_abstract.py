#!/usr/bin/env python3

import os


class Model:
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
    item_type = "script"

    def __init__(self, scripts=None):
        if scripts is None:
            scripts = dict()
        self.scripts = scripts

    def __iter__(self):
        yield from self.scripts

    def add(self, script):
        """
        Append in Scripts
        :param script:
        :return:
        """
        self.scripts[script.name] = script

    def remove(self, script_name):
        """
        Pop from Scripts
        :param script_name:
        :return:
        """
        self.scripts.pop(script_name)

    def get(self, script):
        """
        Get a particular script from a list of scripts
        :param script: (ScriptAbstract)
        :return: script (ScriptAbstract) or Does not exist Error
        """
        try:
            return self.scripts[script]
        except KeyError as e:
            raise KeyError(str(e) + " not in the model's item list.")


class ScriptAbstract:
    """
    This class is parent class for the scripts eg : scripts/__template__.py
    """

    def __init__(self, source_path, name):
        self.source_path = source_path
        self.module_name = name
        self.module_path = os.path.join(self.source_path, self.module_name)
        self.module_headname = os.path.splitext(self.module_name)[0]
        self.icon = os.path.join(r"C:\Users\youss\Documents\GitHub\Maya-Helper-Interface\icons",
                                 '{0}.{1}'.format(self.module_headname, 'png'))

    def run(self):
        raise NotImplementedError

    def get_name(self):
        return type(self)

    def get_dcc(self):
        raise NotImplementedError

    def get_icon(self):
        pass

    def get_module_basename(self):
        """
        Script module base name
        :return: (str)
        """
        return self.module_name

    def get_module_path(self):
        """
        Script module location
        :return: (str)
        """
        return self.module_path
