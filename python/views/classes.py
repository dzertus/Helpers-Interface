#!/usr/bin/python3

from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore

class ToolButton(QtWidgets.QPushButton):
    def __init__(self, parent, item):
        super().__init__()
        self.active = False
        self.parent = parent
        self.item = item

        self.setStyleSheet("background-color: #36302E;"
                           "border :2px solid ;")
        self.setMinimumSize(120, 40)
        self.setMaximumHeight(40)
        self.setToolTip(self.item.name)

        #Icon
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
        self.parent.switch_view()


class Tab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.resize(300, 200)


class TextEdit(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()
        pass
