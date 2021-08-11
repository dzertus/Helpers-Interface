#!/usr/bin/python3

from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore

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
        self.parent.controller.switch_view(self)

    def set_advanced_view(self, view):
        self.advanced_view = view


class Tab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)

        # Initialize tab
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setStyleSheet("background-color: #36302E;"
                           "border :1px solid ;")

        #Documentation Tab
        self.doc_tab = QtWidgets.QWidget()

        #Source Tab
        self.source_tab = QtWidgets.QWidget()


        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.doc_tab, "Doc")
        self.tabs.addTab(self.source_tab, "Source")


        # Doc Tab
        self.doc_tab.layout = QtWidgets.QVBoxLayout(self)
        self.text_edit_doc = DocTextEdit()
        self.text_edit_doc.setReadOnly(True)
        self.doc_tab.layout.addWidget(self.text_edit_doc)
        self.doc_tab.setLayout(self.doc_tab.layout)

        # Source Tab
        self.source_tab.layout = QtWidgets.QVBoxLayout(self)
        self.text_edit_source = SourceTextEdit()
        self.text_edit_source.setReadOnly(True)
        self.source_tab.layout.addWidget(self.text_edit_source)
        self.source_tab.setLayout(self.source_tab.layout)

        # Add to Widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)



class DocTextEdit(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()
        self.text_color = QtGui.QColor('white')
        self.setTextColor(self.text_color)
        self.setText('Documentation Text')

class SourceTextEdit(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()
        self.text_color = QtGui.QColor('white')
        self.setTextColor(self.text_color)
        self.setText('Source text')