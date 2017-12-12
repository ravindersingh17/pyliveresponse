#    Cross Platform Desktop application for Kayako Live Response
#    Copyright (C) 2008  Kayako Infotech Ltd.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lrmodules.loginEntryDialog import Ui_loginEntryDialog
from lrmodules.loginDataDialog import Ui_loginDataDialog
from lrmodules.aboutDialog import Ui_aboutDialog
from lrmodules.logDialog import Ui_logDialog

from PyQt4 import QtCore,QtGui
import md5,os,pickle,time



#######################################
##Form where account values like url,username etc. are entered
class winloginEntryDialog(QtGui.QDialog):
	def __init__(self,loginValues,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_loginEntryDialog()
		self.ui.setupUi(self)
		self.loginValues=loginValues
		self.isEdit=0
		self.entrySuccess=0
		if self.loginValues!=[[]]:
			self.isEdit=1
			self.ui.accountName.setText(self.loginValues[0][0])
			self.ui.lrURL.setText(self.loginValues[0][1][0])
			self.ui.username.setText(self.loginValues[0][1][1])
			self.ui.oldpassword=self.loginValues[0][1][2]
		QtCore.QObject.connect(self.ui.okButton,QtCore.SIGNAL("clicked()"),self.sendloginData)
		QtCore.QObject.connect(self.ui.cancelButton,QtCore.SIGNAL("clicked()"),self.close)
		
	def closeEvent(self,closeEventHandle):
		if self.entrySuccess==0:
			self.loginValues=[[]]
		closeEventHandle.accept()
		
	def sendloginData(self):
		straccountName=str(self.ui.accountName.text())
		strlrURL=str(self.ui.lrURL.text())
		strusername=str(self.ui.username.text())
		strpassword=str(self.ui.password.text())
		if self.isEdit==1 and strpassword=='':
			strpassword=self.ui.oldpassword
		if straccountName=='' or strlrURL=='' or strusername=='' or strpassword=='':
				print "One of reqired fields Empty"
		else:
			self.loginValues[0]=[straccountName,[strlrURL,strusername,md5.new(strpassword).hexdigest()]]
			self.entrySuccess=1
			self.close()
		
		
		
		
		
#########################################
##Form that displays and allows editing of accounts		
class winloginDataDialog(QtGui.QDialog):
	def __init__(self,loginData,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_loginDataDialog()
		self.ui.setupUi(self)
		self.loginData=loginData
		for account in self.loginData:
			QtGui.QListWidgetItem(account,self.ui.loginDataList)
		QtCore.QObject.connect(self.ui.addButton,QtCore.SIGNAL("clicked()"),self.showEntryDialog)
		QtCore.QObject.connect(self.ui.editButton,QtCore.SIGNAL("clicked()"),self.showEditEntryDialog)
		QtCore.QObject.connect(self.ui.loginDataList,QtCore.SIGNAL("doubleClicked(QModelIndex)"),self.showEditEntryDialog)
		QtCore.QObject.connect(self.ui.deleteButton,QtCore.SIGNAL("clicked()"),self.deleteAccount)
		QtCore.QObject.connect(self.ui.okButton,QtCore.SIGNAL("clicked()"),self.close)
		
	def deleteAccount(self):
		currentAccount=str(self.ui.loginDataList.currentItem().text())
		if currentAccount!='':
			del(self.loginData[currentAccount])
		self.ui.loginDataList.clear()
		for account in self.loginData:
			QtGui.QListWidgetItem(account,self.ui.loginDataList)
	
	def showEntryDialog(self):
		self.loginValues=[[]]
		self.loginEntryDialogInstance=winloginEntryDialog(self.loginValues)
		self.loginEntryDialogInstance.exec_()
		if self.loginValues!=[[]]:
			self.loginData[self.loginValues[0][0]]=self.loginValues[0][1]
		del(self.loginEntryDialogInstance)
		self.ui.loginDataList.clear()
		for account in self.loginData:
			QtGui.QListWidgetItem(account,self.ui.loginDataList)

	def showEditEntryDialog(self):
		currentAccount=str(self.ui.loginDataList.currentItem().text())
		if currentAccount!='':
			self.loginValues=[[currentAccount,self.loginData[currentAccount]]]
			self.loginEntryDialogInstance=winloginEntryDialog(self.loginValues)
			self.loginEntryDialogInstance.exec_()
		
			##Edit info only if dialog box wasn't cancelled
			if self.loginValues!=[[]]:
				del(self.loginData[currentAccount])
				self.loginData[self.loginValues[0][0]]=self.loginValues[0][1]
		
			del(self.loginEntryDialogInstance)
			self.ui.loginDataList.clear()
			for account in self.loginData:
				QtGui.QListWidgetItem(account,self.ui.loginDataList)
	
	
		
###########################################################
##About Dialog
	
class aboutDialog(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_aboutDialog()
		self.ui.setupUi(self)
		
		
###########################################################
##Log window Dialog
		

class logDialog(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_logDialog()
		self.ui.setupUi(self)
		logfile=None
		try:
			logfile=open(os.path.expanduser('~')+'/pyliveresponse_debug.dat','rb')
		except:
			self.ui.logTextEdit.setText("Debug log is unreadable or does not exist")
		
		if logfile!=None:
			try:
				while 1:
					debugData=pickle.load(logfile)
					if debugData['type']=='error':
						messageColor='#aa0000'
					else:
						messageColor='#00aa00'
						
					self.ui.logTextEdit.append("<font color=%s>%s: %s<br/> %s"%(messageColor,
					time.asctime(time.localtime(debugData['timestamp'])),debugData['errormessage'],debugData['details']))
					
			except pickle.PicklingError:
					self.ui.logTextEdit.append("Data Unreadable")
			except EOFError:
					self.ui.logTextEdit.append("--")
