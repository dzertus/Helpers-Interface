#!/usr/bin/env python3

class Controller:
    def __init__(self, model, view):
        print('Initialize Controller')
        self.model = model
        self.view = view

    def run_script(self, item):
        item.run()

    def add_item(self, item):
        self.model.add(item)
        self.view.add_button(item)

    def remove_item(self, item_name):
        try:
            self.model.remove(item_name)
        except KeyError:
            print('This element is not in the list')

    def show_items(self):
        pass
