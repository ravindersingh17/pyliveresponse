# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginDataDialog.ui'
#
# Created: Mon Nov  3 13:41:14 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_loginDataDialog(object):
    def setupUi(self, loginDataDialog):
        loginDataDialog.setObjectName("loginDataDialog")
        loginDataDialog.resize(329, 229)
        self.gridlayout = QtGui.QGridLayout(loginDataDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.okButton = QtGui.QPushButton(loginDataDialog)
        self.okButton.setEnabled(True)
        self.okButton.setObjectName("okButton")
        self.gridlayout.addWidget(self.okButton, 3, 0, 1, 2)
        self.addButton = QtGui.QPushButton(loginDataDialog)
        self.addButton.setObjectName("addButton")
        self.gridlayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.editButton = QtGui.QPushButton(loginDataDialog)
        self.editButton.setObjectName("editButton")
        self.gridlayout.addWidget(self.editButton, 1, 1, 1, 1)
        self.deleteButton = QtGui.QPushButton(loginDataDialog)
        self.deleteButton.setEnabled(True)
        self.deleteButton.setObjectName("deleteButton")
        self.gridlayout.addWidget(self.deleteButton, 2, 1, 1, 1)
        self.loginDataList = QtGui.QListWidget(loginDataDialog)
        self.loginDataList.setObjectName("loginDataList")
        self.gridlayout.addWidget(self.loginDataList, 0, 0, 3, 1)

        self.retranslateUi(loginDataDialog)
        QtCore.QMetaObject.connectSlotsByName(loginDataDialog)

    def retranslateUi(self, loginDataDialog):
        loginDataDialog.setWindowTitle(QtGui.QApplication.translate("loginDataDialog", "Login Data", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("loginDataDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("loginDataDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("loginDataDialog", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("loginDataDialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))

