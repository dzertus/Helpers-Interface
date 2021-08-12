#!/usr/bin/python3

from PySide2 import QtGui
from PySide2 import QtWidgets


class ToolButton(QtWidgets.QPushButton):
    def __init__(self, parent, item):
        super().__init__()
        self.parent = parent
        self.item = item
        self.advanced_view = None

        self.setStyleSheet("background-color: #36302E;"
                           "border :2px solid ;")
        self.setMinimumSize(120, 40)
        self.setMaximumHeight(40)
        self.setToolTip(self.item.name)

        # Icon
        pixmap = QtGui.QPixmap(self.item.icon)
        icon = QtGui.QIcon(pixmap)
        self.setIcon(icon)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtGui.Qt.LeftButton:
            self.button_pressed()
        elif QMouseEvent.button() == QtGui.Qt.RightButton:
            self.switch_view()

    def button_pressed(self):
        """
        Left Click
        Run the function run() of the script Item
        :return:
        """
        self.item.run()

    def switch_view(self):
        """
        Right Click
        Turn on advanced mode
        :return:
        """
        # TODO : Refactor : Remove instance dependency (Call it from the controller instead of this method)
        self.parent.controller.switch_view(self)

    def set_advanced_view(self, view):
        self.advanced_view = view
