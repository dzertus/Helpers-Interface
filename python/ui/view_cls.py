#!/usr/bin/python3

from itertools import cycle

from PySide2 import QtWidgets
from PySide2 import QtCore

from ui.misc_widgets_cls import Tab, MenuBar

class InterfaceAbstract(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QtWidgets.QWidget(self)
        self.setStyleSheet("background-color: #221E1D;"
                           "border :2px solid ;")
        self.create_menu_bar()
        self.set_central_widget()


    def create_menu_bar(self):
        self.main_menu = self.menuBar()
        sources_menu = self.main_menu.addMenu("&Sources")

        self.help_menu = self.menuBar()
        help_menu = self.help_menu.addMenu("&Help")

    def add_btn(self, btn):
        """
        Adds a button to the grid layout , will be visible to the viewer
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        self.container_layout.addWidget(btn)

    def set_window_title(self):
        self.setWindowTitle(self.title)

    def set_central_widget(self):
        self.setCentralWidget(self.central_widget)

    def show_ui(self):
        self.show()

    def hide_ui(self):
        self.hide()

    def get_pos(self):
        return self.pos()

    def switch_view(self, target):
        target.hide_ui()
        self.show_ui()

class DefaultInterface(InterfaceAbstract):
    def __init__(self):
        super().__init__()
        self.title = 'Helpers Interface'
        self.set_window_title()
        self.setFixedHeight(100)
        self.container_layout = QtWidgets.QHBoxLayout(self)

        self.central_widget.setLayout(self.container_layout)

class AdvancedInterface(InterfaceAbstract):
    def __init__(self, data, btn):
        super().__init__()
        self.data = data
        self.btn = btn

        self.resize(600, 400)

        self.container_layout = QtWidgets.QVBoxLayout(self)
        self.container_layout.setAlignment(QtCore.Qt.AlignTop)

        self.tab = Tab()
        self.container_layout.addWidget(self.tab)

        self.central_widget.setLayout(self.container_layout)

    def set_documentation(self):
        method_exists = getattr(self.data, "get_doc", None)
        if method_exists:
            documentation = self.data.get_doc()
            self.tab.text_edit_doc.set_text(documentation)

    def set_source_code(self):
        src_code = open(self.data.get_module_path(), 'r')
        self.tab.text_edit_source.set_text(src_code.read())
