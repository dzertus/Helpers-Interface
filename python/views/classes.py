#!/usr/bin/python3

from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore

from views import text_widgets


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
        self.text_edit_doc = text_widgets.DocTextEdit()
        self.text_edit_doc.setReadOnly(True)
        self.doc_tab.layout.addWidget(self.text_edit_doc)
        self.doc_tab.setLayout(self.doc_tab.layout)

        # Source Tab
        self.source_tab.layout = QtWidgets.QVBoxLayout(self)
        self.text_edit_source = text_widgets.SourceTextEdit()
        self.text_edit_source.setReadOnly(True)
        self.source_tab.layout.addWidget(self.text_edit_source)
        self.source_tab.setLayout(self.source_tab.layout)

        # Add to Widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


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

        single_line_comment_format = QtGui.QTextCharFormat()
        single_line_comment_format.setForeground(QtCore.Qt.red)
        self.highlightingRules.append((QtCore.QRegExp("//[^\n]*"),
                                       single_line_comment_format))

        self.multiLineCommentFormat = QtGui.QTextCharFormat()
        self.multiLineCommentFormat.setForeground(QtCore.Qt.red)

        quotation_format = QtGui.QTextCharFormat()
        quotation_format.setForeground(QtCore.Qt.darkYellow)
        self.highlightingRules.append((QtCore.QRegExp("\".*\""), quotation_format))

        function_format = QtGui.QTextCharFormat()
        function_format.setFontItalic(True)
        function_format.setForeground(QtCore.Qt.cyan)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                                       function_format))

        self.commentStartExpression = QtCore.QRegExp("/\\*")
        self.commentEndExpression = QtCore.QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, frmt in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, frmt)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        start_index = 0
        if self.previousBlockState() != 1:
            start_index = self.commentStartExpression.indexIn(text)

        while start_index >= 0:
            end_index = self.commentEndExpression.indexIn(text, start_index)

            if end_index == -1:
                self.setCurrentBlockState(1)
                comment_length = len(text) - start_index
            else:
                comment_length = end_index - start_index + self.commentEndExpression.matchedLength()

            self.setFormat(start_index, comment_length,
                           self.multiLineCommentFormat)
            start_index = self.commentStartExpression.indexIn(text,
                                                              start_index + comment_length)
