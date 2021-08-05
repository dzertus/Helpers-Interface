import os


class Module:
    def __init__(self, path):
        self.path = path

    def get_name(self):
        return os.path.basename(self.path)

    def get_content(self):
        with open(self.path, 'r') as file:
            content = file.read().replace('\n', '')
        return content

    def get_doc(self):
        pass

    def get_dcc(self):
        pass
