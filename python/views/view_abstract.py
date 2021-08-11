#!/usr/bin/python3

from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore

from collections import defaultdict

from views.classes import ToolButton, Tab


class InterfaceFactory(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.active_view = None

    def add_button(self, item):
        """
        Adds a button to the grid layout , will be visible to the viewer
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        raise NotImplementedError

    def set_window_title(self):
        raise NotImplementedError

    def get_active_button(self):
        raise NotImplementedError

    def hide_ui(self):
        raise NotImplementedError


class NormalInterface(InterfaceFactory):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title = 'Maya Helpers Interface'

        self.set_window_title()

        self.setStyleSheet("background-color: #221E1D;"
                           "border :2px solid ;")
        self.setFixedHeight(70)

        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)

        self.container_layout = QtWidgets.QGridLayout(self)
        centralWidget.setLayout(self.container_layout)
        self.container_layout.setDefaultPositioning(0, QtCore.Qt.Vertical)

    def add_button(self, button):
        self.container_layout.addWidget(button)

    def set_window_title(self):
        self.setWindowTitle(self.title)

    def show_ui(self):
        self.show()

    def hide_ui(self):
        self.hide()

    def set_advanced_view(self, advanced_view):
        self.advanced_view = advanced_view

    def get_pos(self):
        return self.pos()


class AdvancedInterface(InterfaceFactory):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title = 'Maya Helpers Interface Advanced'

        self.set_window_title()

        self.setStyleSheet("background-color: #221E1D;"
                           "border :2px solid ;")
        self.resize(600, 400)

        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)

        self.container_layout = QtWidgets.QVBoxLayout(self)
        self.container_layout.setAlignment(QtCore.Qt.AlignTop)

        self.tab = Tab()
        self.container_layout.addWidget(self.tab)

        centralWidget.setLayout(self.container_layout)

    def add_button(self, button):
        self.button = button
        self.container_layout.addWidget(self.button)

    def set_window_title(self):
        self.setWindowTitle(self.title)

    def show_ui(self):
        self.show()

    def hide_ui(self):
        self.hide()

    def get_pos(self):
        return self.pos()


class InterfaceController:
    def __init__(self):
        print('Initialize View Controller')
        self.normal_view = NormalInterface(self)
        self.normal_view.show()

    def add_button(self, item):
        """
        Creates button for the normal view
        Generates the advanced view for the button
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        #TODO : Refactor
        #Normal View Button
        normal_button = ToolButton(self.normal_view, item)
        self.normal_view.add_button(normal_button)

        #Advanced View
        advanced_view = AdvancedInterface(self)
        advanced_button = ToolButton(advanced_view, item)
        advanced_view.add_button(advanced_button)

        normal_button.set_advanced_view(advanced_view)
        advanced_button.set_advanced_view(advanced_view)

        self.set_documentation(item, advanced_view)
        self.set_source_code(item, advanced_view)


    def get_active_view(self, button):
        #TODO : Refactor
        active_view = None
        if isinstance(button.parent, NormalInterface):
            active_view = self.normal_view
        elif isinstance(button.parent, AdvancedInterface):
            active_view = button.advanced_view
        return active_view

    def switch_view(self, button):
        #TODO : Refactor
        active_view = self.get_active_view(button)
        passive_view = self.normal_view
        if active_view == self.normal_view:
            passive_view = button.advanced_view

        pos = button.parent.get_pos()
        active_view.hide()
        passive_view.move(pos.x(), pos.y())
        passive_view.show()

    def set_documentation(self,item , view):
        documentation = item.get_doc()
        view.tab.text_edit_doc.set_text(documentation)

    def set_source_code(self, item, view):
        source_code = open(item.get_module_path(),'r')
        view.tab.text_edit_source.set_text(source_code.read())