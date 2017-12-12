# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginEntryDialog.ui'
#
# Created: Mon Nov  3 13:59:26 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_loginEntryDialog(object):
    def setupUi(self, loginEntryDialog):
        loginEntryDialog.setObjectName("loginEntryDialog")
        loginEntryDialog.resize(301, 167)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginEntryDialog.sizePolicy().hasHeightForWidth())
        loginEntryDialog.setSizePolicy(sizePolicy)
        self.gridlayout = QtGui.QGridLayout(loginEntryDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.textLabel1 = QtGui.QLabel(loginEntryDialog)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.textLabel2 = QtGui.QLabel(loginEntryDialog)
        self.textLabel2.setWordWrap(False)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.textLabel3 = QtGui.QLabel(loginEntryDialog)
        self.textLabel3.setWordWrap(False)
        self.textLabel3.setObjectName("textLabel3")
        self.gridlayout.addWidget(self.textLabel3, 2, 0, 1, 1)
        self.textLabel4 = QtGui.QLabel(loginEntryDialog)
        self.textLabel4.setWordWrap(False)
        self.textLabel4.setObjectName("textLabel4")
        self.gridlayout.addWidget(self.textLabel4, 3, 0, 1, 1)
        self.accountName = QtGui.QLineEdit(loginEntryDialog)
        self.accountName.setObjectName("accountName")
        self.gridlayout.addWidget(self.accountName, 0, 1, 1, 2)
        self.lrURL = QtGui.QLineEdit(loginEntryDialog)
        self.lrURL.setObjectName("lrURL")
        self.gridlayout.addWidget(self.lrURL, 1, 1, 1, 2)
        self.username = QtGui.QLineEdit(loginEntryDialog)
        self.username.setObjectName("username")
        self.gridlayout.addWidget(self.username, 2, 1, 1, 2)
        self.password = QtGui.QLineEdit(loginEntryDialog)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridlayout.addWidget(self.password, 3, 1, 1, 2)
        self.okButton = QtGui.QPushButton(loginEntryDialog)
        self.okButton.setObjectName("okButton")
        self.gridlayout.addWidget(self.okButton, 4, 1, 1, 1)
        self.cancelButton = QtGui.QPushButton(loginEntryDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.gridlayout.addWidget(self.cancelButton, 4, 2, 1, 1)

        self.retranslateUi(loginEntryDialog)
        QtCore.QMetaObject.connectSlotsByName(loginEntryDialog)

    def retranslateUi(self, loginEntryDialog):
        loginEntryDialog.setWindowTitle(QtGui.QApplication.translate("loginEntryDialog", "Enter Login Information", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("loginEntryDialog", "Account Name", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2.setText(QtGui.QApplication.translate("loginEntryDialog", "Live Response URL", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel3.setText(QtGui.QApplication.translate("loginEntryDialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel4.setText(QtGui.QApplication.translate("loginEntryDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("loginEntryDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("loginEntryDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

