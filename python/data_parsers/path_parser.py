"""
Parsing method for modules collection
"""
import os
import logging
import re

logger = logging.getLogger('path_parser')

class PathParser:
    def __init__(self, config):
        self.config = config
        self.sources = self.config['sources']

    def add_source(self, new_src, config_path):
        if not new_src in self.sources:
            self.sources.append(new_src)
            self.config['sources'] = self.sources
            config_utils.save_yaml(config_path, self.config)
        else:
            logger.info('{} already exists as a source, will not be added to config'.format(new_src))

    def get_sources(self):
        return self.sources

    def get_directories_from_source(self, source):
        """
        List of directories
        :return: (lst)
        """
        for (root, dirs, files) in os.walk(source):
            return dirs

    def get_exension_type(self, extension):
        module_valid_ext = self.config['extentions']['module_valide_ext']
        icon_valid_ext = self.config['extentions']['icon_valid_ext']

        if extension in module_valid_ext:
            return 'module'
        if extension in icon_valid_ext:
            return 'icon'

    def get_module_name(self, fullname):
        result = re.search(self.config['regex']['module_file_sanity_name'], fullname)
        return result.group(1)

    def is_dir_valid(self, dir):
        if not dir.startswith(self.config['extentions']['application_ext']):
            logger.info('{} does not start with "hi", it is skipped'.format(dir))
            return False
        elif dir.startswith('__'):
            logger.info('{} starts with "__", it is skipped'.format(dir))
            return False
        else:
            return True

    def is_file_valid(self, file):
        regex_file_sanity = re.compile(self.config['regex']['module_file_sanity_name'])
        if not file.startswith(self.config['extentions']['application_ext']):
            logger.info('{} does not start with "hi", it is skipped'.format(file))
            return False
        elif file.startswith('__'):
            logger.info('{} starts with "__", it is skipped'.format(file))
            return False
        elif regex_file_sanity.match(file) == None:
            logger.info('{} does not match naming convention, example : hi_example.ext'.format(file))
        else:
            return True

    def is_extension_valid(self, extension):
        module_valid_ext = self.config['extentions']['module_valide_ext']
        icon_valid_ext = self.config['extentions']['icon_valid_ext']

        if extension in set(module_valid_ext + icon_valid_ext):
            return True
        else:
            return False

    def is_source_already_exists(self, source):
        exists = False
        if source in self.sources:
            exists = True
        return exists

    def get_scripts_from_source(self, source):
        dir_data = dict()
        dirs = self.get_directories_from_source(source)
        for d in dirs:
            valid = self.is_dir_valid(d)
            if valid == False:
                continue
            files = os.listdir(os.path.join(source, d))
            for f in files:
                valid = self.is_file_valid(f)
                if valid == False:
                    continue
                module_name = self.get_module_name(f)
                extension = os.path.splitext(f)[1]
                valid = self.is_extension_valid(extension)
                if valid == False:
                    continue
                if not module_name in dir_data.keys():
                    dir_data[module_name] = dict()
                ext_type = self.get_exension_type(extension)
                dir_data[module_name]['name'] = module_name
                dir_data[module_name]['dir'] = os.path.join(source, d)
                dir_data[module_name][ext_type] = f
        return dir_data