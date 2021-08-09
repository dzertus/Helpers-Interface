#!/usr/bin/python3
# -*- coding : utf-8 -*-

import sys
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore


class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world - pythonprogramminglanguage.com")

        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)

        self.gridLayout = QtWidgets.QGridLayout(self)
        centralWidget.setLayout(self.gridLayout)


    def start(self):
        print('Opening the view')

    def add_button(self, item):
        pixmap = QtGui.QPixmap(item.icon)
        icon = QtGui.QIcon(pixmap)
        button = ToolButton(item.icon)
        button.setIcon(icon)
        self.gridLayout.addWidget(button)

        button.setText('')
        button.setMaximumSize(50, 50)

        button.show()

class ToolButton(QtWidgets.QPushButton):
    def __init__(self, name):
        super().__init__()
        self.setText(name)

