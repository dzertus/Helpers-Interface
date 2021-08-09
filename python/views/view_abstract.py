#!/usr/bin/python3
# -*- coding : utf-8 -*-

from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore


class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maya Helpers Interface")

        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)

        self.gridLayout = QtWidgets.QGridLayout(self)
        centralWidget.setLayout(self.gridLayout)
        self.gridLayout.setDefaultPositioning(0, QtCore.Qt.Vertical)

    def start(self):
        print('Opening the view')

    def add_button(self, item):

        button = ToolButton(item)
        self.gridLayout.addWidget(button)
        button.setText('')
        button.setMaximumSize(50, 50)

        button.show()



class ToolButton(QtWidgets.QPushButton):
    def __init__(self, item):
        super().__init__()
        self.item = item
        self.setText(self.item.name)

        #Icon
        pixmap = QtGui.QPixmap(self.item.icon)
        icon = QtGui.QIcon(pixmap)
        self.setIcon(icon)

        #Function
        self.clicked.connect(self.button_pressed)

    def button_pressed(self):
        self.item.run()

