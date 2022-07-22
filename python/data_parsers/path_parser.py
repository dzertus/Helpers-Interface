"""
Parsing Method for modules collection
"""
import os


class PathParser:

    def new_root(self, root):
        """
        Sets a new path
        Refresh files with callback
        :param root: (str)
        :return: (str)
        """
        self.root = root

    def get_files(self):
        """
        List of .py files
        :return: (str)
        """
        return os.listdir(self.root)

    def get_modules(self):
        """
        Absolute path of the module
        :return: (str)
        """

        files = self.get_files()
        modules = dict()
        modules['root'] = self.root
        modules['files'] = list()

        for m_file in files:
            if not m_file.startswith('__'):
                modules['files'].append(m_file)
        print('Modules ', modules)
        return modules
