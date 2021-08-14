#!/usr/bin/python3

from PySide2 import QtWidgets
from PySide2 import QtCore

from views.classes import Tab

class InterfaceAbstract(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QtWidgets.QWidget(self)
        self.active_view = None
        self.setStyleSheet("background-color: #221E1D;"
                           "border :2px solid ;")
        self.set_central_widget()

    def add_button(self, item):
        """
        Adds a button to the grid layout , will be visible to the viewer
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        raise NotImplementedError

    def set_window_title(self):
        self.setWindowTitle(self.title)

    def set_central_widget(self):
        self.setCentralWidget(self.central_widget)

    def get_active_button(self):
        raise NotImplementedError

    def hide_ui(self):
        raise NotImplementedError

    def get_pos(self):
        raise NotImplementedError


class NormalInterface(InterfaceAbstract):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title = 'Maya Helpers Interface'
        self.set_window_title()

        self.setFixedHeight(70)

        self.container_layout = QtWidgets.QGridLayout(self)
        self.container_layout.setDefaultPositioning(0, QtCore.Qt.Vertical)
        self.central_widget.setLayout(self.container_layout)

        self.advanced_view = None

    def add_button(self, button):
        self.container_layout.addWidget(button)

    def show_ui(self):
        self.show()

    def hide_ui(self):
        self.hide()

    def get_active_button(self):
        pass

    def set_advanced_view(self, advanced_view):
        self.advanced_view = advanced_view

    def get_pos(self):
        return self.pos()


class AdvancedInterface(InterfaceAbstract):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title = 'Maya Helpers Interface Advanced'

        self.set_window_title()

        self.resize(600, 400)

        self.container_layout = QtWidgets.QVBoxLayout(self)
        self.container_layout.setAlignment(QtCore.Qt.AlignTop)

        self.tab = Tab()
        self.container_layout.addWidget(self.tab)

        self.central_widget.setLayout(self.container_layout)

    def add_button(self, button):
        self.container_layout.addWidget(button)

    def show_ui(self):
        self.show()

    def get_active_button(self):
        pass

    def hide_ui(self):
        self.hide()

    def get_pos(self):
        return self.pos()
