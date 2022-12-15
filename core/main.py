# Open file


import importlib
import os
import sys

from data import path, env, config as uc
from utils import logs as ul
from utils import request


# Install Environment
installed = False


NAME = 'HINTERFACE'
ENV = env.Env(NAME)

if env.Env.PATH is not None:
    if env.Env.PATH not in sys.path:
        sys.path.insert(0, env.Env.PATH)

    # Config
    conf_path = os.path.join(env.Env.DEFAULT_CONF_FILE)
    if not os.path.exists(conf_path):
        request.download_file(default_config_url, env.Env.DEFAULT_CONF_FILE)

    config_parser = uc.YamlParser(env.Env.DEFAULT_CONF_FILE)
    config = config_parser.load()

    # Setup optional settings
    settings = config['settings']
    ENV.set_optional_settings(settings)


    # Setup main config
    app_config = config['app']
    parser = path.PathParser(app_config)

    # Setup env config
    env_config = config['env']
    for env_var in env_config:
        ENV.set_env_var(env_var.value())
    import pprint
    #pprint.pprint(config)
    pprint.pprint(os.environ)

    # Setup logs config
    log_config = config['logs']
    logger_inst = ul.Log(__name__, log_config)

    logger = logger_inst.logger
    logger.debug('Parsing default_source data')

    # Gathering sources
    logger.info('Gathering default_source locations')
    sources = parser.get_sources()
    scripts = []
    installed = True

else:
    # Ask user to install PATH env variable
    print('Please install this environment variable : \n'
          'HINTERFACE as name \n'
          'Source code python path : '
          '..Helpers-Interface-initialize_python2/python as value\n'
          'For more informations on how to install an environment variable '
          'according to your OS , visit this page : \n'
          'https://github.com/dzertus/Helpers-Interface/blob/main/README.md#maya-helper-interface\n'
          )
    # Shut down process because PATH env variable not found
    # Todo Open dialog to set

def run(scripts=None):
    """
    :param scripts:
    :return:
    """
    logger.error()
    logger.info('...Init App')

    model = model_cls.ScriptModel()

    # application
    logger.info(f'Running on : {sys.executable}')
    # app = QtWidgets.QApplication(sys.argv)

    # handler
    h = handler_cls.Handler(model)
    h.run()

    for s in scripts:
        h.add_item(s)
        logger.debug(f'"{s.name}" script added')

    logger.info('Running...')
    sys.exit(app.exec_())


def main():
    """

    :return:
    """
    if installed is True:
        for src in sources:
            if os.path.isdir(src):
                src_data = parser.get_scripts_from_source(src)
            else:
                raise OSError(f'Config not found, looking for:\n\t {src}\nDo you want to back up a config file ? ')
            for script_name in src_data.keys():
                module_path = os.path.join(src_data[script_name]['dir'], src_data[script_name]['module'])
                spec = importlib.util.spec_from_file_location(script_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                script = module.Script(src, src_data[script_name])
                scripts.append(script)

        run(scripts)
    else:
        print('Shutting down..')
        sys.exit()

if __name__ == '__main__':
    main()
