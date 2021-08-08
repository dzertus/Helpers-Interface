#!/usr/bin/env python3

class Controller:
    def __init__(self, model, view):
        print('Initialize Controller')
        self.model = model
        self.view = view

    def add_item(self, item):
        self.model.add(item)

    def remove_item(self, item_name):
        try:
            self.model.remove(item_name)
        except KeyError:
            print('This element is not in the list')

    def show_items(self):
        items = list(self.model)
        item_type = self.model.item_type
        self.view.show_item_list(item_type, items)

    def show_item_information(self, item_name):
        try:
            item_info = self.model.get(item_name)
        except Exception:
            item_type = self.model.item_type
            self.view.item_not_found(item_type, item_name)
        else:
            item_type = self.model.item_type
            self.view.show_item_information(item_type, item_name, item_info)
