#!/usr/bin/env python3

import logging

from ui.view_cls import DefaultInterface, AdvancedInterface
from ui.btn_cls import ToolButton
from third_party.errors import *

logger = logging.getLogger('baseLogger')

class Handler():
    def __init__(self, model, view):
        super().__init__()

        logger.debug('Initialize Handler')
        self.model = model
        self.default_view = view

    def run_ui(self):
        self.default_view.show()

    def set_documentation(self, item, view):
        method_exists = getattr(item, "get_doc", None)
        if method_exists:
            documentation = item.get_doc()
            view.tab.text_edit_doc.set_text(documentation)

    def set_source_code(self, item, view):
        source_code = open(item.get_module_path(), 'r')
        view.tab.text_edit_source.set_text(source_code.read())

    def create_button(self, item):
        button = ToolButton(self, item)
        return button

    def create_advanced_view(self, button):
        advanced_view = AdvancedInterface()
        advanced_view.add_button(button)
        button.set_advanced_view(advanced_view)
        advanced_view.setWindowTitle(button.item.name)
        self.set_documentation(button.item, advanced_view)
        self.set_source_code(button.item, advanced_view)

    def add_item(self, item):
        self.model.add(item)
        self.add_button(item)

    def add_button(self, item):
        """
        Creates button for the normal view
        Generates the advanced view for the button
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        # Create button
        tool_button = self.create_button(item)
        self.default_view.add_button(tool_button)

    def switch_view(self, button):
        # Switch to advanced view
        if button.advanced_mode == False:
            logger.debug('Switch to Advanced with : {}'.format(button.item.name))
            self.default_view.hide()
            if button.advanced_view is None:
                self.create_advanced_view(button)
            else:
                raise ViewNotFoundError
            button.advanced_view.show_ui()
            button.advanced_mode = True
        # Switch to normal view
        else:
            logger.debug('Switch to Normal with : {}'.format(button.item.name))
            button.advanced_view.hide()
            self.default_view.show_ui()
            button.advanced_mode = False
