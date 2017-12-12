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

from xml.etree import ElementTree as ET
from xml.parsers.expat import ExpatError
import re
import random
import zlib



class lrxmlengine:
	def __init__(self):
		self.useoldchat=False
		
	def uncompressdata(self,serverdata):
		try:
			datachunks=serverdata.split(';',5)
			if datachunks[0]=='compressed':
				datachunks[-1]=zlib.decompress(datachunks[-1])
			
			##Hack to work around a bug with html escaping
			datachunks[-1]=datachunks[-1].replace('&','&amp;')
			xmldataroot=ET.XML(datachunks[-1])
			return xmldataroot
		except ExpatError,error:
			return (-1,str(error))
			
		
	def categorytodict(self,xmldataroot,predefined):
		for subelement in xmldataroot:
			if subelement.tag=='category':
				predefined.append({'type':'category','title':subelement.attrib['title'],'child':[]})
				self.categorytodict(subelement,predefined[-1]['child'])
			elif subelement.tag=='entry':
				predefined.append({'type':'entry','title':subelement.attrib['title'],'entrytype':subelement.attrib['type'],
				'data':subelement.text})
				
		
	def parselogindata(self,serverdata):
		xmldataroot=self.uncompressdata(serverdata)
		if xmldataroot[0]==-1:
			return [-1,xmldataroot[1]]
		self.lrversion=xmldataroot.find('version').text
		self.lrversion=self.lrversion.split('.')
		if self.lrversion[0]!='3':
			return [-1, "You are using an unsupported version of LiveResponse"]
		if int(self.lrversion[1])>=20:
			uniqueid=xmldataroot.find('uniqueid').text
		else:
			uniqueid=''
			self.useoldchat=True
		sessionid=xmldataroot.find('sessionid').text
		staffsessionid=xmldataroot.find('staffsessionid').text
		
		predefined=[]
		self.categorytodict(xmldataroot,predefined)
		return([0,sessionid,staffsessionid,uniqueid,predefined])
	
	
	##Visitor parsing function, leaves out a lot of info(TODO section)
	def parsevisitordata(self,serverdata):
		xmldataroot=self.uncompressdata(serverdata)
		if xmldataroot[0]==-1:
			return [-1,xmldataroot[1]]
		#parseresult={'visitor':{},'staff':{},'pendingchat':{},'chatexec':{}}
		parseresult={}
		pendingchatcount=1
		staffcount=1
		for subelement in xmldataroot:
			
			if subelement.tag not in parseresult:
				parseresult[subelement.tag]={}
			if subelement.tag=='visitor':
				identifier=subelement.find('sessionid').text
				
			elif subelement.tag=='staff':
				identifier=(subelement.find('staffusername').text).lower()
				
			elif subelement.tag=='pendingchat':
				identifier=subelement.find('chatsessionid').text
				
			elif subelement.tag=='chatexec':
				identifier=subelement.find('chatsessionid').text
				
			else:
				identifier=str(random.random())
			
			parseresult[subelement.tag][identifier]={}
			
			for dataelement in subelement:
				if dataelement.text:
					parseresult[subelement.tag][identifier][dataelement.tag]=dataelement.text
					
		
		return [1,parseresult]
			
		

		
	def parsestartchatdata(self,serverdata):
		if int(self.lrversion[1])<10:
			regexmatchurl=re.search('iframe src=\"index\.php(.*?)\"',serverdata)
		else:
			regexmatchurl=re.search('loadXMLHTTPRequest\(\"index\.php(.*?)\"',serverdata)
		if regexmatchurl==None:
			return([-1,"Unknown Server Response"])
		regexmatchdiv=re.search('<div id=\"buffer\".*?</div>',serverdata)
		if regexmatchdiv==None:
			return ([0,(regexmatchurl.group(1),'')])
		return ([0,(regexmatchurl.group(1),regexmatchdiv.group(0))])
	
	def parsechatdata(self,serverdata):
		if self.useoldchat:
			return self.parsechatdataold(serverdata)
		parseresult=[]
		
		try:
			xmldata=ET.XML(serverdata)
		except ExpatError,error:
			return([-1,str(error)])
		
		for chatchunk in xmldata:
			chunkdata={}
			for chunk in chatchunk:
				chunkdata[chunk.tag]=chunk.text
			parseresult.append(chunkdata)
		return ([1,parseresult])
			
	
	##Function that handles chats for versions prior to 3.20.02
	def parsechatdataold(self,serverdata):
		
		parseresult=[]
		chatmessages=re.findall(r'writeToDiv\(\"(.*?)<BR />\"\);',serverdata)
		for message in chatmessages:
			chatchunks=re.findall(r'<span class=\'(.*?)\'>(.*?)</span>',message)
			if chatchunks[0][0]=='clientname':
				parseresult.append({'clientname':chatchunks[0][1][:-1]})
			parseresult[-1]['type']=chatchunks[1][0]
			if chatchunks[1][0]=='clientmessage':
				parseresult[-1]['message']=chatchunks[1][1][18:-6]            #Remove the javascript HTML stuff to get to the text
		return [1,parseresult]
			
	def getstafftostaffchatid(self,serverdata):
		datachunks=serverdata.split(';',5)
		if datachunks[0]=='compressed':
			datachunks[-1]=zlib.decompress(datachunks[-1])
		if len(datachunks[-1])!=32:
			return[-1,'']
		return [1,datachunks[-1]]
		
				
			
		