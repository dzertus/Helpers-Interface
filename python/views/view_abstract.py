#!/usr/bin/python3
# -*- coding : utf-8 -*-

import sys
from PySide2 import QtGui
from PySide2 import QtWidgets


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Maya Helpers Interface')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.resize(700, 50)
        self.setMinimumHeight(50)
        self.setMinimumWidth(350)

        self.grid_layout = QtWidgets.QGridLayout()

class ToolButton(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        pass
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec_())