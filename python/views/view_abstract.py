#!/usr/bin/python3
# -*- coding : utf-8 -*-

from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore


class NormalInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.active_view = False

        self.setWindowTitle("Maya Helpers Interface")
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


class AdvancedInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.active_view = False

        self.item = item

        self.setStyleSheet("background-color: #36302E;"
                           "border :2px solid ;")

        self.setMinimumSize(120, 40)
        self.setMaximumSize(120, 40)
        self.setToolTip(self.item.name)

        #Icon
        pixmap = QtGui.QPixmap(self.item.icon)
        icon = QtGui.QIcon(pixmap)
        self.setIcon(icon)

class ToolButton(QtWidgets.QPushButton):
    def __init__(self, item):
        super().__init__()
        self.active = False
        self.item = item

        self.setStyleSheet("background-color: #36302E;"
                           "border :2px solid ;")
        self.setMinimumSize(120, 40)
        self.setMaximumSize(120, 40)
        self.setToolTip(self.item.name)

        #Icon
        pixmap = QtGui.QPixmap(self.item.icon)
        icon = QtGui.QIcon(pixmap)
        self.setIcon(icon)

    def add_button(self, item):
        """
        Adds a button to the grid layout , will be visible to the viewer
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        button = ToolButton(item)
        self.gridLayout.addWidget(button)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtGui.Qt.LeftButton:
            self.button_pressed()
        elif QMouseEvent.button() == QtGui.Qt.RightButton:
            print("Opening Advanced")
            self.switch_advanced()

    def button_pressed(self):
        """
        Left Click
        Run the function run of the script Item
        :return:
        """
        self.item.run()

    def switch_advanced(self):
        """
        Right Click
        Turn on advanced mode
        :return:
        """
        self.active = True


class ViewsController:
    def __init__(self):
        print('Initialize View Controller')
        self.normal_view = None
        self.advanced_view = None

    def add_button(self, item):
        """
        Adds a button to the grid layout , will be visible to the viewer
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        self.active_view.add_button(item)

    def refresh(self):
        self.active_view.show()

    def initialize_normal_view(self):-
        self.normal_view = NormalInterface()
        self.active_view = self.normal_view
        self.refresh()

    def initialize_advanced_view(self):
        self.advanced_view = AdvancedInterface()
        self.active = self.advanced_view
        self.refresh()

    def show_normal_view(self):
        self.normal_view.show()

    def show_advanced_view(self):
        self.advanced_view.show()

    def switch_view(self):
        pass