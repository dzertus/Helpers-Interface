#!/usr/bin/python3

from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore

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
        self.parent.switch_view()