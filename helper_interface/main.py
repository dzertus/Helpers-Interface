import importlib
import os
import sys

from data import path, config as uc
from utils import logs as ul
from utils import request


def install_env():
    """

    :return:
    """
    HINTERFACE = os.environ.get('HINTERFACE')
    if HINTERFACE is None:
        # Ask user to install HINTERFACE env variable
        print('Please install this environment variable : \n'
              'HINTERFACE as name \n'
              'Source code python path : '
              '..Helpers-Interface-initialize_python2/python as value\n'
              'For more informations on how to install an environment variable '
              'according to your OS , visit this page : \n'
              'https://github.com/dzertus/Helpers-Interface/blob/main/README.md#maya-helper-interface\n'
              )
        # Shut down process because HINTERFACE env variable not found
        # Todo Open dialog to set
        print('Shutting down process')
        sys.exit()

    if not HINTERFACE in sys.path:
        sys.path.insert(0, HINTERFACE)


def run(scripts=None):
    """
    :param scripts:
    :return:
    """

    logger.error()
    logger.info('...Init App')

    model = model_cls.ScriptModel()

    # application
    logger.info('Running on : {}'.format(sys.executable))
    ''
    # app = QtWidgets.QApplication(sys.argv)

    # handler
    h = handler_cls.Handler(model)
    h.run()

    for s in scripts:
        h.add_item(s)
        logger.debug('"{}" script added'.format(s.name))

    logger.info('Running...')
    sys.exit(app.exec_())


def main():
    """

    :return:
    """
    cfg_path = os.path.join(HINTERFACE, '../conf/config.yaml')
    default_config_url = os.path.join(HINTERFACE, 'conf/config.yaml')
    if not os.path.exists(cfg_path):
        request.download_file(default_config_url, cfg_path)

    config_parser = uc.YamlParser(cfg_path)
    config = config_parser._load_yaml()
    # pprint.pprint(config)
    # Setup main config
    main_config = config['main']
    parser = path.PathParser(main_config)

    # Setup logs config
    log_config = config['logs']
    logger_inst = ul.Log(__name__, log_config)

    logger = logger_inst.logger
    logger.debug('Parsing default_source data')

    # Gathering sources
    logger.info('Gathering default_source locations')
    sources = parser.get_sources()
    scripts = []

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


if __name__ == '__main__':
    main()
