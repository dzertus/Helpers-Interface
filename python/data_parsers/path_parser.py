"""
Parsing Method for modules collection
"""
import os


class PathParser:
    def __init__(self, path):
        if path is None:
            return
        if os.path.exists(path) is False:
            if path is not None:
                raise OSError('Path does not exist')

        self.path = self.new_path(path)
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
        self.files = self.get_files()

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
        return [m_file for m_file in self.files if not m_file.startswith('__')]
