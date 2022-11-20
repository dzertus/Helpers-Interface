#!/usr/bin/python3

#exec(open(r"C:\Users\youss\Documents\GitHub\Helpers-Interface\launcher.py").read())
import sys
import os
import logging

#Todo : Python 2
import importlib


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

## Setup Config File
CONFIG_PATH = os.path.join(HI_PYTHONPATH, 'config.yaml')

## Setup Logging
# Logger instance
logs.run_logger()
logger = logging.getLogger('launcher')

logger.debug('Parsing scripts data')

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
    # Setup config
    config = config_utils.load_yaml(CONFIG_PATH)
    parser = path_parser.PathParser(config)

    # Add native source path
    native_source_path = os.path.join(HI_PYTHONPATH, 'scripts')
    parser.add_source(native_source_path, CONFIG_PATH)
    sources = parser.get_sources()

    scripts = []

    for src in sources:
        if os.path.isdir(src):
            dir_data = parser.get_scripts_from_source(src)

        for script_name in dir_data.keys():
            module_path = os.path.join(dir_data[script_name]['dir'], dir_data[script_name]['module'])
            spec = importlib.util.spec_from_file_location(script_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            script = module.Script(src, dir_data[script_name])
            scripts.append(script)

    run(scripts)

if __name__ == '__main__':
    main()

