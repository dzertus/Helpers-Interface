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

        # Icon
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
        # TODO : Refactor : Remove instance dependency (Call it from the controller instead of this method)
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

        # Documentation Tab
        self.doc_tab = QtWidgets.QWidget()

        # Source Tab
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
        self.highlighter = Highlighter(self.text_edit_source.document())

        self.text_edit_source.setReadOnly(True)
        self.source_tab.layout.addWidget(self.text_edit_source)
        self.source_tab.setLayout(self.source_tab.layout)

        # Add to Widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class DocTextEdit(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()
        self.text_color = QtGui.QColor('grey')
        self.setTextColor(self.text_color)

    def set_text(self, text):
        self.setText(text)


class SourceTextEdit(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()
        self.text_color = QtGui.QColor('grey')
        self.setTextColor(self.text_color)

    def set_text(self, text):
        self.setPlainText(text)


class Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        keyword_format = QtGui.QTextCharFormat()
        keyword_format.setForeground(QtCore.Qt.green)
        keyword_format.setFontWeight(QtGui.QFont.Bold)

        keyword_patterns = ["\\bchar\\b", "\\bclass\\b", "\\bconst\\b",
                            "\\bdouble\\b", "\\benum\\b", "\\bexplicit\\b", "\\bfriend\\b",
                            "\\binline\\b", "\\bint\\b", "\\blong\\b", "\\bnamespace\\b",
                            "\\boperator\\b", "\\bprivate\\b", "\\bprotected\\b",
                            "\\bpublic\\b", "\\bshort\\b", "\\bsignals\\b", "\\bsigned\\b",
                            "\\bslots\\b", "\\bstatic\\b", "\\bstruct\\b",
                            "\\btemplate\\b", "\\btypedef\\b", "\\btypename\\b",
                            "\\bunion\\b", "\\bunsigned\\b", "\\bvirtual\\b", "\\bvoid\\b",
                            "\\bvolatile\\b"]

        self.highlightingRules = [(QtCore.QRegExp(pattern), keyword_format)
                                  for pattern in keyword_patterns]

        class_format = QtGui.QTextCharFormat()
        class_format.setFontWeight(QtGui.QFont.Bold)
        class_format.setForeground(QtCore.Qt.green)
        self.highlightingRules.append((QtCore.QRegExp("\\bQ[A-Za-z]+\\b"),
                                       class_format))

        singleLineCommentFormat = QtGui.QTextCharFormat()
        singleLineCommentFormat.setForeground(QtCore.Qt.red)
        self.highlightingRules.append((QtCore.QRegExp("//[^\n]*"),
                                       singleLineCommentFormat))

        self.multiLineCommentFormat = QtGui.QTextCharFormat()
        self.multiLineCommentFormat.setForeground(QtCore.Qt.red)

        quotationFormat = QtGui.QTextCharFormat()
        quotationFormat.setForeground(QtCore.Qt.darkYellow)
        self.highlightingRules.append((QtCore.QRegExp("\".*\""), quotationFormat))

        functionFormat = QtGui.QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(QtCore.Qt.cyan)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                                       functionFormat))

        self.commentStartExpression = QtCore.QRegExp("/\\*")
        self.commentEndExpression = QtCore.QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                           self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                                                             startIndex + commentLength)
