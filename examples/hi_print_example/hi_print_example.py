"""

"""

from models import models

class Script(models.ScriptAbstract):
    def __init__(self, source_path, script_data):
        super(Script, self).__init__(source_path, script_data)
        self.name = script_data['name']
        print('Install {}'.format(self.name))
        self.dcc = ['maya']

    def get_name(self):
        return self.name

    def get_dcc(self):
        return self.dcc

    def get_icon(self):
        pass

    def get_doc(self):
        return 'This script prints Example'

    def run(self):
        """
        Script Main Function
        """
        print('Example')