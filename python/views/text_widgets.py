#!/usr/bin/python3

from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore

from views import classes

class TextEditAbstract(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()
        self.text_color = QtGui.QColor('grey')
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
        self.highlighter = classes.Highlighter(self.document())

    def set_text(self, text):
        self.setPlainText(text)
