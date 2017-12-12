# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logDialog.ui'
#
# Created: Mon Jan 19 15:12:20 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_logDialog(object):
    def setupUi(self, logDialog):
        logDialog.setObjectName("logDialog")
        logDialog.resize(618, 547)
        self.gridLayout = QtGui.QGridLayout(logDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.logTextEdit = QtGui.QTextEdit(logDialog)
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setObjectName("logTextEdit")
        self.gridLayout.addWidget(self.logTextEdit, 0, 0, 1, 1)

        self.retranslateUi(logDialog)
        QtCore.QMetaObject.connectSlotsByName(logDialog)

    def retranslateUi(self, logDialog):
        logDialog.setWindowTitle(QtGui.QApplication.translate("logDialog", "Debug Log", None, QtGui.QApplication.UnicodeUTF8))

