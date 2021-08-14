#!/usr/bin/env python3

import os


class Env:
    def __init__(self):
        print('Environment Parser Initialized')

    def add_path_variable(self, name, path):
        os.environ[name] = path
