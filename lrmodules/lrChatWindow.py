# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lrChatWindow.ui'
#
# Created: Wed Nov  5 18:04:46 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_lrChatWindow(object):
    def setupUi(self, lrChatWindow):
        lrChatWindow.setObjectName("lrChatWindow")
        lrChatWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(lrChatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.chatTextArea = QtGui.QTextEdit(self.centralwidget)
        self.chatTextArea.setReadOnly(True)
        self.chatTextArea.setObjectName("chatTextArea")
        self.gridLayout.addWidget(self.chatTextArea, 0, 0, 1, 2)
        self.chatInputBox = QtGui.QLineEdit(self.centralwidget)
        self.chatInputBox.setObjectName("chatInputBox")
        self.gridLayout.addWidget(self.chatInputBox, 1, 0, 1, 1)
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        self.sendButton.setObjectName("sendButton")
        self.gridLayout.addWidget(self.sendButton, 1, 1, 1, 1)
        lrChatWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(lrChatWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName("menubar")
        lrChatWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(lrChatWindow)
        self.statusbar.setObjectName("statusbar")
        lrChatWindow.setStatusBar(self.statusbar)

        self.retranslateUi(lrChatWindow)
        QtCore.QMetaObject.connectSlotsByName(lrChatWindow)

    def retranslateUi(self, lrChatWindow):
        lrChatWindow.setWindowTitle(QtGui.QApplication.translate("lrChatWindow", "Chat Window", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("lrChatWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))

