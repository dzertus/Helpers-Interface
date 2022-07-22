#!/usr/bin/python3

from PySide2.QtGui import QColor
from PySide2.QtWidgets import QTextEdit

from ui import misc_widgets_cls


class TextEditAbstract(QTextEdit):
    def __init__(self):
        super().__init__()
        self.text_color = QColor('grey')
        self.setTextColor(self.text_color)

    def set_text(self, text):
        raise NotImplementedError


class DocTextEdit(TextEditAbstract):
    def __init__(self):
        super().__init__()

    def set_text(self, text):
        self.setText(text)


class SourceTextEdit(TextEditAbstract):
    def __init__(self):
        super().__init__()

        # Set highlighter
        self.highlighter = misc_widgets_cls.Highlighter(self.document())

    def set_text(self, text):
        self.setPlainText(text)
