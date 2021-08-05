"""
Parsing Method for modules collection
"""
import os

class ParserPath:
    def __init__(self, path):
        self.path = path
        self.files = self.get_files()
        self.modules = self.get_modules()

    def new_path(self, path):
        """
        - Sets a new path
        - Refresh files with callback
        :param path: (str)
        :return: (str)
        """
        self.path = path


    def get_files(self):
        """
        - List of .py files
        :return: (str)
        """
        return os.listdir(self.path)

    def get_modules(self):
        """
        Absolute path of the module
        :return: (str)
        """
        return [os.path.join(self.path, m_file) for m_file in self.files if not m_file.startswith('__')]

