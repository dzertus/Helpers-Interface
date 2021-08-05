from abc import ABC, abstractmethod
from collections import defaultdict

class Model(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def get(self, item):
        """Returns an object with a .items() call method
        that iterates over key,value pairs of its information."""
        pass

    @property
    @abstractmethod
    def item_type(self):
        pass

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

        pass

    def remove(self, script_name):
        """
        Pop from Scripts
        :param product_name:
        :return:
        """

    def get(self, script):
        try:
            return self.scripts[script]
        except KeyError as e:
            raise KeyError(str(e) + " not in the model's item list.")

class Script:
    def __init__(self, name, content, doc, dcc):
        self.name = name
        self.content = content
        self.doc = doc
        self.dcc = dcc
        print ('Script {} created'.format(self.name))

    def __getattr__(self, attr_name):
       return self[attr_name]
