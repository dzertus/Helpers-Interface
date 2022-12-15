# Template file
"""
Parsing method for modules collection
"""
import os
import logging
import re

from data import config as uc

logger = logging.getLogger('path_parser')


def get_directories_from_source(source):
    """
    List of directories
    :return: (lst)
    """
    for (root, dirs, files) in os.walk(source):
        return dirs


class PathParser:
    """
    Path Parser
    """

    def __init__(self):
        """

        """
        self.sources = []

    def add_source(self, new_src, config_path, config):
        """

        :param new_src:
        :param config_path:
        :return:
        """

        if not new_src in self.sources:
            self.sources.append(new_src)
            config['sources'] = self.sources
            uc.save_yaml(config_path, config)
        else:
            logger.info(
                    f'{new_src} already exists as a source, will not be added to config')

    def get_sources(self):
        """

        :return:
        """
        return self.sources

    def get_exension_type(self, extension):
        """

        :param extension:
        :return:
        """
        module_valid_ext = self.config['extentions']['module_valide_ext']
        icon_valid_ext = self.config['extentions']['icon_valid_ext']

        if extension in module_valid_ext:
            return 'module'
        if extension in icon_valid_ext:
            return 'icon'

    def get_module_name(self, fullname):
        """

        :param fullname:
        :return:
        """
        result = re.search(self.config['regex']['module_file_sanity_name'], fullname)
        return result.group(1)

    def is_dir_valid(self, directory):
        """

        :param directory:
        :return:
        """
        if not directory.startswith(self.config['extentions']['application_ext']):
            logger.info(f'{directory} does not start with "hi", it is skipped')
            return False
        elif directory.startswith('__'):
            logger.info(f'{directory} starts with "__", it is skipped')
            return False
        else:
            return True

    def is_file_valid(self, file):
        """

        :param file:
        :return:
        """
        regex_file_sanity = re.compile(self.config['regex']['module_file_sanity_name'])
        if not file.startswith(self.config['extentions']['application_ext']):
            logger.info(f'{file} does not start with "hi", it is skipped')
            return False
        elif file.startswith('__'):
            logger.info(f'{file} starts with "__", it is skipped')
            return False
        elif regex_file_sanity.match(file) == None:
            logger.info(
                    f'{file} does not match naming convention, example : hi_example.ext')
        else:
            return True

    def is_extension_valid(self, extension):
        """

        :param extension:
        :return:
        """
        module_valid_ext = self.config['extentions']['module_valide_ext']
        icon_valid_ext = self.config['extentions']['icon_valid_ext']

        if extension in set(module_valid_ext + icon_valid_ext):
            return True
        else:
            return False

    def is_source_already_exists(self, source):
        """

        :param source:
        :return:
        """
        exists = False
        if source in self.sources:
            exists = True
        return exists

    def get_scripts_from_source(self, source):
        """

        :param source:
        :return:
        """
        dir_data = dict()
        dirs = get_directories_from_source(source)
        for d in dirs:
            valid = self.is_dir_valid(d)
            if valid is False:
                continue
            files = os.listdir(os.path.join(source, d))
            for f in files:
                valid = self.is_file_valid(f)
                if not valid:
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
