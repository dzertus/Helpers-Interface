"""
Models
"""
import os


class Model:
    """
    Model
    """
    def __iter__(self):
        """

        :return:
        """
        raise NotImplementedError

    def get(self, item):
        """
        Returns an object with a .items() call method
        that iterates over key,value pairs of its information.
        :param item:
        :return:
        """
        raise NotImplementedError

    @property
    def item_type(self):
        """

        :return:
        """
        raise NotImplementedError


class ScriptModel(Model):
    """
    ScriptModel
    """
    item_type = "script"

    def __init__(self, scripts=None):
        """

        :param scripts:
        """
        if scripts is None:
            scripts = {}
        self.scripts = scripts

    def __iter__(self):
        """

        :return:
        """
        yield self.scripts

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
        Get a particular script from a list of default_source
        :param script: (ScriptAbstract)
        :return: script (ScriptAbstract) or Does not exist Error
        """
        try:
            return self.scripts[script]
        except KeyError as e:
            raise KeyError(str(e) + " not in the model's item list.")


class ScriptAbstract:
    """
    This class is parent class for the default_source eg : default_source/__template__.py
    """
    def __init__(self, source_path, script_data):
        """

        :param source_path:
        :param script_data:
        """
        self.source_path = source_path
        self.module_name = script_data['module']
        self.module_path = os.path.join(script_data['dir'], self.module_name)
        self.module_headname = script_data['name']
        self.icon_path = os.path.join(script_data['dir'], script_data['icon'])

    def run(self):
        """

        :return:
        """
        raise NotImplementedError

    def get_name(self):
        """

        :return:
        """
        return type(self)

    def get_dcc(self):
        """

        :return:
        """
        raise NotImplementedError

    def get_icon(self):
        """

        :return:
        """
        pass

    def get_module_basename(self):
        """
        Script module base name
        :return:
        """
        return self.module_name

    def get_module_path(self):
        """
        Script module location
        :return: (str)
        """
        return self.module_path
