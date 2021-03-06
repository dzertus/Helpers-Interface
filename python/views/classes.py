#!/usr/bin/python3

from PySide2.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont
from PySide2.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from PySide2.QtCore import Qt, QRegExp

from views.text_widgets import DocTextEdit, SourceTextEdit


class Tab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        # Initialize tab
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("background-color: #36302E;"
                                "border :1px solid ;")

        # Documentation Tab
        self.doc_tab = QWidget()

        # Source Tab
        self.source_tab = QWidget()

        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.doc_tab, "Doc")
        self.tabs.addTab(self.source_tab, "Source")

        # Doc Tab
        self.doc_tab.layout = QVBoxLayout(self)
        self.text_edit_doc = DocTextEdit()
        self.text_edit_doc.setReadOnly(True)
        self.doc_tab.layout.addWidget(self.text_edit_doc)
        self.doc_tab.setLayout(self.doc_tab.layout)

        # Source Tab
        self.source_tab.layout = QVBoxLayout(self)
        self.text_edit_source = SourceTextEdit()
        self.text_edit_source.setReadOnly(True)
        self.source_tab.layout.addWidget(self.text_edit_source)
        self.source_tab.setLayout(self.source_tab.layout)

        # Add to Widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.green)
        keyword_format.setFontWeight(QFont.Bold)

        keyword_patterns = ["\\bchar\\b", "\\bclass\\b", "\\bconst\\b",
                            "\\bdouble\\b", "\\benum\\b", "\\bexplicit\\b", "\\bfriend\\b",
                            "\\binline\\b", "\\bint\\b", "\\blong\\b", "\\bnamespace\\b",
                            "\\boperator\\b", "\\bprivate\\b", "\\bprotected\\b",
                            "\\bpublic\\b", "\\bshort\\b", "\\bsignals\\b", "\\bsigned\\b",
                            "\\bslots\\b", "\\bstatic\\b", "\\bstruct\\b",
                            "\\btemplate\\b", "\\btypedef\\b", "\\btypename\\b",
                            "\\bunion\\b", "\\bunsigned\\b", "\\bvirtual\\b", "\\bvoid\\b",
                            "\\bvolatile\\b"]

        self.highlightingRules = [(QRegExp(pattern), keyword_format)
                                  for pattern in keyword_patterns]

        class_format = QTextCharFormat()
        class_format.setFontWeight(QFont.Bold)
        class_format.setForeground(Qt.green)
        self.highlightingRules.append((QRegExp("\\bQ[A-Za-z]+\\b"),
                                       class_format))

        single_line_comment_format = QTextCharFormat()
        single_line_comment_format.setForeground(Qt.red)
        self.highlightingRules.append((QRegExp("//[^\n]*"),
                                       single_line_comment_format))

        self.multiLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.red)

        quotation_format = QTextCharFormat()
        quotation_format.setForeground(Qt.darkYellow)
        self.highlightingRules.append((QRegExp("\".*\""), quotation_format))

        function_format = QTextCharFormat()
        function_format.setFontItalic(True)
        function_format.setForeground(Qt.cyan)
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                                       function_format))

        self.commentStartExpression = QRegExp("/\\*")
        self.commentEndExpression = QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, frmt in self.highlightingRules:
            expression = QRegExp(pattern)
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
