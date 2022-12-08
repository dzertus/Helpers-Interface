#!/usr/bin/python2

import sys
import os
import logging
import importlib

from utils import logs as ul

from data_parsers import path, config as uc

## Install Environment Variable
# Gets HI_PYTHONPATH env variable , if not existing, asking user to add this env variable
HI_PYTHONPATH = os.environ.get('HI_PYTHONPATH')
if HI_PYTHONPATH == None:
    # Ask user to install HI_PYTHONPATH env variable
    print('Please install this environment variable : \n '
          'HI_PYTHONPATH as name \n'
          'Source code python path : ..Helpers-Interface-initialize_python2/python as value\n'
          'For more informations on how to install an environment variable according to your OS , visit this page : \n'
          'https://github.com/dzertus/Helpers-Interface/blob/main/README.md#maya-helper-interface\n'
          )

    # Shot down process because HI_PYTHONPATH env variable not found
    print('Shutting down process')
    sys.exit()


if not HI_PYTHONPATH in sys.path:
    sys.path.insert(0, HI_PYTHONPATH)

def run(scripts=None):
    logger.info('...Init App')

    model = model_cls.ScriptModel()

    # application
    logger.info('Running on : {}'.format(sys.executable))
    current_app = ''
    #app = QtWidgets.QApplication(sys.argv)

    # handler
    h = handler_cls.Handler(model)
    h.run()

    for s in scripts:
        h.add_item(s)
        logger.debug('"{}" script added'.format(s.name))

    logger.info('Running...')
    sys.exit(app.exec_())

def main():

    cfg_path = os.path.join(HI_PYTHONPATH, 'config.yaml')
    config = uc.load_yaml(cfg_path)
    # Setup config
    main_config = config['main']
    parser = path.PathParser(main_config)
    sources = parser.get_sources()


    # Setup Logging
    log_config = config['log']
    logger_inst = ul.Log(__name__, log_config)
    logger = logger_inst.logger
    logger.debug('Parsing scripts data')



    scripts = []
    src_data = None
    for src in sources:
        if os.path.isdir(src):
            src_data = parser.get_scripts_from_source(src)
        else:
            raise OSError('Config not found, looking for:\n\t {}'.format(src))
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

