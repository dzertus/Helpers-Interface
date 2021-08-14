#!/usr/bin/python3

from PySide2.QtGui import QPixmap, Qt
from PySide2.QtWidgets import QPushButton


class ToolButton(QPushButton):
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
        pixmap = QPixmap(self.item.icon)
        icon = (pixmap)
        self.setIcon(icon)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_pressed()
        elif QMouseEvent.button() == Qt.RightButton:
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
