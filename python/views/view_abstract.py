#!/usr/bin/python3

from abc import ABC, abstractmethod

from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore

from views.classes import ToolButton


class InterfaceAbstract(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.active_view = None

    @abstractmethod
    def set_window_title(self):
        pass

    @abstractmethod
    def close_ui(self):
        pass


class NormalInterface(InterfaceAbstract):
    def __init__(self):
        super().__init__()
        self.title = 'Maya Helpers Interface'

        self.set_window_title()

        self.setStyleSheet("background-color: #221E1D;"
                           "border :2px solid ;")

        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)

        self.gridLayout = QtWidgets.QGridLayout(self)
        centralWidget.setLayout(self.gridLayout)
        self.gridLayout.setDefaultPositioning(0, QtCore.Qt.Vertical)

    def add_button(self, item):
        """
        Adds a button to the grid layout , will be visible to the viewer
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        button = ToolButton(item)
        self.gridLayout.addWidget(button)

    def set_window_title(self):
        self.setWindowTitle(self.title)

    def get_active_button(self):
        pass

    def close_ui(self):
        self.close()


class AdvancedInterface(InterfaceAbstract):
    def __init__(self, item):
        super().__init__()
        self.title = 'Maya Helpers Interface Advanced'

        self.item = item
        self.set_window_title()
        self.setStyleSheet("background-color: #36302E;"
                           "border :2px solid ;")

        self.setMinimumSize(120, 40)
        self.setMaximumSize(120, 40)
        self.setToolTip(self.item.name)

        #Icon
        pixmap = QtGui.QPixmap(self.item.icon)
        icon = QtGui.QIcon(pixmap)
        self.setIcon(icon)

    def set_window_title(self):
        self.setWindowTitle(self.title)

    def get_active_button(self):
        pass

    def close_ui(self):
        self.close()


class ViewsController:
    def __init__(self):
        print('Initialize View Controller')
        self.normal_view = None
        self.advanced_view = None
        self.views = [self.normal_view, self.advanced_view]

    def add_button(self, item):
        """
        Adds a button to the grid layout , will be visible to the viewer
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        self.active_view.add_button(item)

    def show_normal_view(self):
        if self.normal_view == None:
            self.normal_view = NormalInterface()
        self.active_view = self.normal_view
        self.inactive_view = self.advanced_view
        self.normal_view.show()

    def show_advanced_view(self):
        if self.advanced_view == None:
            self.advanced_view = AdvancedInterface()
        self.active_view = self.advanced_view
        self.inactive_view = self.normal_view
        self.advanced_view.show()

    def switch_view(self):
        print('switching view')
        self.inactive_view.close()
        self.active_view.show()