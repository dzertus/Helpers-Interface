"""
Env
"""
import logging
import os


class Env(object):
    CORE = 'core'
    CONF = 'conf'
    LOGS = 'logs'

    def __init__(self, name, **settings):
        """
        Init
        :param name:
        """
        print('Initializing Environment')

        # Set mendatory settings
        Env.NAME = name
        Env.PATH = os.environ.get(Env.NAME, None)

        # Set optional settings
        if settings:
            self.set_optional_settings(settings)

        # Set mendatory folders
        Env.CORE_PATH = self.set_env_var(Env.CORE)
        Env.CONF_PATH = self.set_env_var(Env.CONF)
        Env.LOGS_PATH = self.set_env_var(Env.LOGS)

        # Set mendatory files
        Env.DEFAULT_CONF_FILE = self.set_env_var('DEFAULT_CONF_FILE',
                                                 custom_value=os.path.join(Env.CONF_PATH,
                                                                        'config.yaml'))

        Env.DEFAULT_CACHE_FILE = self.set_env_var('DEFAULT_CACHE_FILE',
                                                  custom_value=os.path.join(Env.CONF_PATH,
                                                                        'cache.yaml'))

        Env.DEFAULT_LOGS_FILE = self.set_env_var('DEFAULT_LOGS_FILE',
                                                  custom_value=os.path.join(Env.LOGS_PATH,
                                                                        'default.log'))


    def set_optional_settings(self, settings=None):
        # Nickname
        Env.NICKNAME = settings['nickname'] or Env.NAME.lower()
        Env.DEFAULT_LOGS_FILE = self.set_env_var('NICKNAME',
                                                  custom_value=Env.NICKNAME)
        print('DONE')

    def is_path_valid(self, path):
        """

        :param path:
        :return:
        """
        valid = True
        # Critic validation
        if path is None:
            valid = False
            ValueError(f'Invalid path: \n\t{path}')
        # Warning validation
        if os.path.exists(path) is False:
            logging.warning(f'File path does not exist: \n\t{path}')
        return valid

    def add_prefix(self, input, prefix=None):
        """

        :param input:
        :param prefix:
        :return:
        """
        if prefix is None:
            prefix = Env.NAME
        prefix = prefix.upper()
        full_name = '_'.join([prefix, input])
        return full_name

    def set_env_var(self, var_name, custom_value=None):
        """

        :param var_name:
        :param over_path:
        :return:
        """

        if custom_value is None:
            value = os.path.join(Env.PATH, var_name)
        else:
            value = custom_value

        var_name = self.add_prefix(var_name)
        os.environ[var_name] = value
        return value