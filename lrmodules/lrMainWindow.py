# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lrMainWindow.ui'
#
# Created: Tue Nov 11 18:53:56 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_lrMainWindow(object):
    def setupUi(self, lrMainWindow):
        lrMainWindow.setObjectName("lrMainWindow")
        lrMainWindow.resize(1280, 970)
        self.centralwidget = QtGui.QWidget(lrMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.staffList = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.staffList.sizePolicy().hasHeightForWidth())
        self.staffList.setSizePolicy(sizePolicy)
        self.staffList.setMaximumSize(QtCore.QSize(200, 16777215))
        self.staffList.setObjectName("staffList")
        self.gridLayout.addWidget(self.staffList, 1, 0, 1, 1)
        self.visitorAreaFrame = QtGui.QFrame(self.centralwidget)
        self.visitorAreaFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.visitorAreaFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.visitorAreaFrame.setLineWidth(0)
        self.visitorAreaFrame.setObjectName("visitorAreaFrame")
        self.visitorTableWidget = QtGui.QTableWidget(self.visitorAreaFrame)
        self.visitorTableWidget.setGeometry(QtCore.QRect(11, 11, 1029, 653))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.visitorTableWidget.sizePolicy().hasHeightForWidth())
        self.visitorTableWidget.setSizePolicy(sizePolicy)
        self.visitorTableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.visitorTableWidget.setLineWidth(1)
        self.visitorTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.visitorTableWidget.setTabKeyNavigation(False)
        self.visitorTableWidget.setAlternatingRowColors(True)
        self.visitorTableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.visitorTableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.visitorTableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.visitorTableWidget.setShowGrid(True)
        self.visitorTableWidget.setColumnCount(7)
        self.visitorTableWidget.setObjectName("visitorTableWidget")
        self.visitorTableWidget.setColumnCount(7)
        self.visitorTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(6, item)
        self.visitorTabWidget = QtGui.QTabWidget(self.visitorAreaFrame)
        self.visitorTabWidget.setGeometry(QtCore.QRect(10, 670, 278, 239))
        self.visitorTabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.visitorTabWidget.setObjectName("visitorTabWidget")
        self.informationTab = QtGui.QWidget()
        self.informationTab.setObjectName("informationTab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.informationTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.visitorInformationTextEdit = QtGui.QTextEdit(self.informationTab)
        self.visitorInformationTextEdit.setReadOnly(True)
        self.visitorInformationTextEdit.setObjectName("visitorInformationTextEdit")
        self.horizontalLayout.addWidget(self.visitorInformationTextEdit)
        self.visitorTabWidget.addTab(self.informationTab, "")
        self.chatStatusTab = QtGui.QWidget()
        self.chatStatusTab.setObjectName("chatStatusTab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.chatStatusTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.visitorChatStatusTextEdit = QtGui.QTextEdit(self.chatStatusTab)
        self.visitorChatStatusTextEdit.setReadOnly(True)
        self.visitorChatStatusTextEdit.setObjectName("visitorChatStatusTextEdit")
        self.horizontalLayout_2.addWidget(self.visitorChatStatusTextEdit)
        self.visitorTabWidget.addTab(self.chatStatusTab, "")
        self.gridLayout.addWidget(self.visitorAreaFrame, 1, 1, 3, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pendingChatList = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pendingChatList.sizePolicy().hasHeightForWidth())
        self.pendingChatList.setSizePolicy(sizePolicy)
        self.pendingChatList.setMaximumSize(QtCore.QSize(200, 150))
        self.pendingChatList.setObjectName("pendingChatList")
        self.gridLayout.addWidget(self.pendingChatList, 3, 0, 1, 1)
        lrMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(lrMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 29))
        self.menubar.setObjectName("menubar")
        lrMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(lrMainWindow)
        self.statusbar.setObjectName("statusbar")
        lrMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(lrMainWindow)
        self.visitorTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(lrMainWindow)

    def retranslateUi(self, lrMainWindow):
        lrMainWindow.setWindowTitle(QtGui.QApplication.translate("lrMainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("lrMainWindow", "Staff", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("lrMainWindow", "Chatter ID", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("lrMainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("lrMainWindow", "Department", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("lrMainWindow", "Operator", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("lrMainWindow", "Wait Time", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("lrMainWindow", "Current Page", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("lrMainWindow", "Country", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTabWidget.setTabText(self.visitorTabWidget.indexOf(self.informationTab), QtGui.QApplication.translate("lrMainWindow", "Information", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTabWidget.setTabText(self.visitorTabWidget.indexOf(self.chatStatusTab), QtGui.QApplication.translate("lrMainWindow", "Chat Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("lrMainWindow", "Pending Chats", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lrMainWindow.ui'
#
# Created: Fri Nov 14 12:34:06 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_lrMainWindow(object):
    def setupUi(self, lrMainWindow):
        lrMainWindow.setObjectName("lrMainWindow")
        lrMainWindow.resize(1280, 970)
        self.centralwidget = QtGui.QWidget(lrMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.staffList = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.staffList.sizePolicy().hasHeightForWidth())
        self.staffList.setSizePolicy(sizePolicy)
        self.staffList.setMaximumSize(QtCore.QSize(200, 16777215))
        self.staffList.setObjectName("staffList")
        self.gridLayout.addWidget(self.staffList, 1, 0, 1, 1)
        self.visitorAreaFrame = QtGui.QFrame(self.centralwidget)
        self.visitorAreaFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.visitorAreaFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.visitorAreaFrame.setLineWidth(0)
        self.visitorAreaFrame.setObjectName("visitorAreaFrame")
        self.visitorTableWidget = QtGui.QTableWidget(self.visitorAreaFrame)
        self.visitorTableWidget.setGeometry(QtCore.QRect(11, 11, 1029, 653))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.visitorTableWidget.sizePolicy().hasHeightForWidth())
        self.visitorTableWidget.setSizePolicy(sizePolicy)
        self.visitorTableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.visitorTableWidget.setLineWidth(1)
        self.visitorTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.visitorTableWidget.setTabKeyNavigation(False)
        self.visitorTableWidget.setAlternatingRowColors(True)
        self.visitorTableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.visitorTableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.visitorTableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.visitorTableWidget.setShowGrid(True)
        self.visitorTableWidget.setColumnCount(7)
        self.visitorTableWidget.setObjectName("visitorTableWidget")
        self.visitorTableWidget.setColumnCount(7)
        self.visitorTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.visitorTableWidget.setHorizontalHeaderItem(6, item)
        self.visitorTabWidget = QtGui.QTabWidget(self.visitorAreaFrame)
        self.visitorTabWidget.setGeometry(QtCore.QRect(10, 670, 278, 239))
        self.visitorTabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.visitorTabWidget.setObjectName("visitorTabWidget")
        self.informationTab = QtGui.QWidget()
        self.informationTab.setObjectName("informationTab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.informationTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.visitorInformationTextEdit = QtGui.QTextEdit(self.informationTab)
        self.visitorInformationTextEdit.setReadOnly(True)
        self.visitorInformationTextEdit.setObjectName("visitorInformationTextEdit")
        self.horizontalLayout.addWidget(self.visitorInformationTextEdit)
        self.visitorTabWidget.addTab(self.informationTab, "")
        self.chatStatusTab = QtGui.QWidget()
        self.chatStatusTab.setObjectName("chatStatusTab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.chatStatusTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.visitorChatStatusTextEdit = QtGui.QTextEdit(self.chatStatusTab)
        self.visitorChatStatusTextEdit.setReadOnly(True)
        self.visitorChatStatusTextEdit.setObjectName("visitorChatStatusTextEdit")
        self.horizontalLayout_2.addWidget(self.visitorChatStatusTextEdit)
        self.visitorTabWidget.addTab(self.chatStatusTab, "")
        self.gridLayout.addWidget(self.visitorAreaFrame, 1, 1, 3, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pendingChatList = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pendingChatList.sizePolicy().hasHeightForWidth())
        self.pendingChatList.setSizePolicy(sizePolicy)
        self.pendingChatList.setMaximumSize(QtCore.QSize(200, 150))
        self.pendingChatList.setObjectName("pendingChatList")
        self.gridLayout.addWidget(self.pendingChatList, 3, 0, 1, 1)
        lrMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(lrMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 29))
        self.menubar.setObjectName("menubar")
        lrMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(lrMainWindow)
        self.statusbar.setObjectName("statusbar")
        lrMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(lrMainWindow)
        self.visitorTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(lrMainWindow)

    def retranslateUi(self, lrMainWindow):
        lrMainWindow.setWindowTitle(QtGui.QApplication.translate("lrMainWindow", "Live Response", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("lrMainWindow", "Staff", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("lrMainWindow", "Chatter ID", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("lrMainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("lrMainWindow", "Department", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("lrMainWindow", "Operator", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("lrMainWindow", "Wait Time", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("lrMainWindow", "Current Page", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTableWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("lrMainWindow", "Country", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTabWidget.setTabText(self.visitorTabWidget.indexOf(self.informationTab), QtGui.QApplication.translate("lrMainWindow", "Information", None, QtGui.QApplication.UnicodeUTF8))
        self.visitorTabWidget.setTabText(self.visitorTabWidget.indexOf(self.chatStatusTab), QtGui.QApplication.translate("lrMainWindow", "Chat Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("lrMainWindow", "Pending Chats", None, QtGui.QApplication.UnicodeUTF8))

