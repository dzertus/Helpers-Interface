#!/usr/bin/python3

from itertools import cycle

from PySide2 import QtWidgets
from PySide2 import QtCore

from views.classes import Tab

class InterfaceAbstract(QtWidgets.QMainWindow):
    views = list()
    views_cycle = cycle(views)
    def __init__(self):
        super().__init__()
        self.central_widget = QtWidgets.QWidget(self)
        self.setStyleSheet("background-color: #221E1D;"
                           "border :2px solid ;")
        self.set_central_widget()

    def add_button(self, button):
        """
        Adds a button to the grid layout , will be visible to the viewer
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        self.container_layout.addWidget(button)

    def set_window_title(self):
        self.setWindowTitle(self.title)

    def set_central_widget(self):
        self.setCentralWidget(self.central_widget)

    def show_ui(self):
        self.show()

    def hide_ui(self):
        self.hide()

    def get_pos(self):
        return self.pos()

class NormalInterface(InterfaceAbstract):
    def __init__(self):
        super().__init__()
        self.views.append(self)
        self.title = 'Helpers Interface'
        self.set_window_title()
        self.setFixedHeight(70)

        self.container_layout = QtWidgets.QGridLayout(self)
        self.container_layout.setDefaultPositioning(0, QtCore.Qt.Vertical)
        self.central_widget.setLayout(self.container_layout)
        self.buttons = list()

    def add_button(self, button):
        """
        Adds a button to the grid layout , will be visible to the viewer
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        self.container_layout.addWidget(button)
        self.buttons.append(button)

class AdvancedInterface(InterfaceAbstract):
    def __init__(self):
        super().__init__()
        self.views.append(self)
        self.resize(600, 400)

        self.container_layout = QtWidgets.QVBoxLayout(self)
        self.container_layout.setAlignment(QtCore.Qt.AlignTop)

        self.tab = Tab()
        self.container_layout.addWidget(self.tab)

        self.central_widget.setLayout(self.container_layout)
        self.buttons = list()

    def add_button(self, button):
        """
        Adds a button to the grid layout , will be visible to the viewer
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        self.container_layout.addWidget(button)
        self.buttons.append(button)



