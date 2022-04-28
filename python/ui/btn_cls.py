#!/usr/bin/python3

from PySide2.QtGui import QPixmap, Qt
from PySide2.QtWidgets import QPushButton

from ui import view_cls

class ToolButton(QPushButton):
    """
    Custom Button
    """
    def __init__(self):
        """
        :param item: Script: Script Object
        """
        super().__init__()
        self.adv_view = None
        self.adv_mod = False
        self.setStyleSheet("background-color: #36302E;"
                           "border :2px solid ;")
        self.setMinimumSize(120, 40)
        self.setMaximumHeight(40)

    def add_item(self, item):
        self.item = item
        self.setToolTip(self.item.name)
        pixmap = QPixmap(self.item.icon)
        icon = (pixmap)
        self.setIcon(icon)

    def set_handler(self, handler):
        self.handler = handler

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.run_item()
        elif QMouseEvent.button() == Qt.RightButton:
            self.switch_view()

    def run_item(self):
        """
        Left Click
        Run the function run() of the script Item
        :return:
        """
        self.item.run()

    def switch_view(self):
        self.handler.switch_view(self)

    def set_advanced_view(self, view):
        self.adv_view = view

    def gen_adv_view(self):
        """
        Generates an advanced view for the button
        :return:
        """
        self.adv_view = view_cls.AdvancedInterface(self.item, self)
        self.adv_view.add_btn(self)
        self.adv_view.setWindowTitle(self.item.name)

        self.adv_view.set_documentation()
        self.adv_view.set_source_code()