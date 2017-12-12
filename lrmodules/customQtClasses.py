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


from PyQt4 import QtGui,QtCore

class customListWidgetItem(QtGui.QListWidgetItem):
	def __init__(self,sessionid,text,parent=None):
		QtGui.QListWidgetItem.__init__(self,text,parent)
		self.sessionid=sessionid

class customIconListWidgetItem(QtGui.QListWidgetItem):
	def __init__(self,sessionid,icon,text,parent=None):
		QtGui.QListWidgetItem.__init__(self,icon,text,parent)
		self.sessionid=sessionid


		
		
class customTableWidgetItem(QtGui.QTableWidgetItem):
	def __init__(self,sessionid,text):
		QtGui.QTableWidgetItem.__init__(self,text)
		self.sessionid=sessionid