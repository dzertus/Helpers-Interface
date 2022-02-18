#!/usr/bin/env python3

import sys

from PySide2.QtWidgets import QApplication

from views.view_abstract import NormalInterface, AdvancedInterface
from views.button_widgets import ToolButton

class ControllerAbstract:
    def __init__(self):
        pass

    def add_item(self, item):
        raise NotImplementedError

    def switch_view(self, button):
        pass

class ClassicController(ControllerAbstract):
    def __init__(self, model, view):
        super().__init__()

        self.app = QApplication(sys.argv)
        print('Initialize Controller')
        self.model = model
        self.normal_view = NormalInterface(self)
        self.normal_view.show()

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
        # TODO : Refactor
        # Normal View Button
        normal_button = ToolButton(self.normal_view, item)
        self.normal_view.add_button(normal_button)

        # Advanced View
        advanced_view = AdvancedInterface(self)
        advanced_button = ToolButton(advanced_view, item)
        advanced_view.add_button(advanced_button)

        normal_button.set_advanced_view(advanced_view)
        advanced_button.set_advanced_view(advanced_view)

        self.set_documentation(item, advanced_view)
        self.set_source_code(item, advanced_view)

    def get_active_view(self, button):
        # TODO : Refactor
        active_view = None
        if isinstance(button.parent, NormalInterface):
            active_view = self.normal_view
        elif isinstance(button.parent, AdvancedInterface):
            active_view = button.advanced_view
        return active_view

    def switch_view(self, button):
        # TODO : Refactor
        active_view = self.get_active_view(button)
        passive_view = self.normal_view
        if active_view == self.normal_view:
            passive_view = button.advanced_view

        pos = button.parent.get_pos()
        active_view.hide()
        passive_view.move(pos.x(), pos.y())
        passive_view.show()

    def set_documentation(self, item, view):
        method_exists = getattr(item, "get_doc", None)
        if method_exists:
            documentation = item.get_doc()
            view.tab.text_edit_doc.set_text(documentation)

    def set_source_code(self, item, view):
        source_code = open(item.get_module_path(), 'r')
        view.tab.text_edit_source.set_text(source_code.read())

