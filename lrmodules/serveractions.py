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


import urllib,urllib2,cookielib
import threading,Queue


def createrequest(url,values=None):
	if values:
		data=urllib.urlencode(values)
		return(urllib2.Request(url,data))
	return(urllib2.Request(url))


	

class getserverresponse(threading.Thread):
	def __init__(self,server_request,lrbrowser,typeofrequest,identifier,serverqueue):
		self.server_request=server_request
		self.lrbrowser=lrbrowser
		self.serverqueue=serverqueue
		self.typeofrequest=typeofrequest
		self.identifier=identifier
		threading.Thread.__init__(self)
			
	def run(self):
		try:
			serverobj=self.lrbrowser.open(self.server_request)
			raw_response=serverobj.read()
			self.serverqueue.put({'result':'success',
			'typeofrequest':self.typeofrequest,
			'identifier':self.identifier,
			'data':raw_response})
			
			
		except IOError,error:
			self.serverqueue.put({'result':'fail','error':str(error)})
			
		except ValueError,error:
			self.serverqueue.put({'result':'fail','error':error})



class serverengine:
	def __init__(self,product_url,username,md5_password,default_status,randno):
		self.product_url=product_url
		self.session_url=product_url+'winapp/index.php?_randomnumber='+randno
		self.username=username
		self.password=md5_password
		self.status=default_status
		self.randno=randno
		self.cookiestore = cookielib.CookieJar()
		self.authhandler = urllib2.HTTPBasicAuthHandler()
		self.authhandler.add_password(realm='SupportSuite',
                          uri='http://172.16.0.216',
                          user='test',
                          passwd='test')
		self.lrbrowser = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookiestore), self.authhandler)
		self.lrbrowser.addheaders=[('User-agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.1)')]
		self.serverqueue=Queue.Queue()	
	
			
	def setsessionvariables(self,sessionid,staffsessionid,uniqueid):
		self.sessionid=sessionid
		self.staffsessionid=staffsessionid
		self.uniqueid=uniqueid
		
		
			
	def getserverdata(self):
		try:
			serverresponse=self.serverqueue.get(False)
			return(serverresponse)
		except Queue.Empty:
			return('')
	
	def login(self):
		login_values={'_ca':'login',
		'username':self.username,
		'password':self.password,
		'randno':self.randno}
		login_request=createrequest(self.session_url,login_values)
		getserverresponse(login_request,self.lrbrowser,'login','',self.serverqueue).start()
		serverresponse=self.serverqueue.get(True)
		return(serverresponse)
	
	def logout(self):
		logout_values={'_ca':'logout',
		'username':self.username,
		'sessionid':self.sessionid,
		'staffsessionid':self.staffsessionid,
		'randno':self.randno}
		logout_request=createrequest(self.session_url,logout_values)
		getserverresponse(logout_request,self.lrbrowser,'logout','',self.serverqueue).start()
		
		
	
	def fetchvisitors(self):
		fetchvisitorvalues={'_m':'livesupport',
		'_a':'fetchvisitors',
		'sessionid':self.sessionid,
		'randno':self.randno,
		'status':self.status}
		visitorrequest=createrequest(self.session_url,fetchvisitorvalues)
		getserverresponse(visitorrequest,self.lrbrowser,'visitor','',self.serverqueue).start()
		
	def startchat(self,chatsessionid,visitorsessionid='',visitorname=''):
		chat_request=createrequest(self.session_url+
		'&_m=livesupport&_a=startstaffchat&utf8=1'+
		'&chatsessionid='+chatsessionid+
		'&visitorsessionid='+visitorsessionid+
		'&sessionid='+self.sessionid)
		getserverresponse(chat_request,self.lrbrowser,'startchat',(chatsessionid,visitorsessionid,visitorname),self.serverqueue).start()
		
	def refusechat(self,chatsessionid):
		refuse_values={
		'_m':'livesupport',
		'_a':'refusechat',
		'utf8':'1',
		'chatsessionid':chatsessionid,
		'sessionid':self.sessionid}
		refuse_request=createrequest(self.session_url,refuse_values)
		getserverresponse(refuse_request,self.lrbrowser,'refusechat',chatsessionid,self.serverqueue).start()
		
	def startstafftostaffchat(self,staffid,staffusername):
		staffchat_values={'_m':'livesupport',
		'_a':'startstafftostaffchat',
		'utf8':'1',
		'staffid':staffid,
		'sessionid':self.sessionid}
		staffchat_request=createrequest(self.session_url,staffchat_values)
		getserverresponse(staffchat_request,self.lrbrowser,'stafftostaff',(staffid,staffusername),self.serverqueue).start()
		
	def chatendsession(self,chatsessionid):
		endchat_values={'_m':'livesupport',
		'_a':'chatendsession',
		'utf8':'1',
		'chatsessionid':chatsessionid,
		'sessionid':self.sessionid}
		endchat_request=createrequest(self.session_url,endchat_values)		
		getserverresponse(endchat_request,self.lrbrowser,'endchat',chatsessionid,self.serverqueue).start()
	
	def sendmessage(self,chatmessage,chatsessionid):
		message_values={'_m':'livesupport',
		'_a':'postchatmessage',
		'message':chatmessage,
		'chatsessionid':chatsessionid,
		'base64':'true',
		'utf8':'1',
		'sessionid':self.sessionid}
		message_request=createrequest(self.session_url,message_values)
		getserverresponse(message_request,self.lrbrowser,'chatmessage',chatsessionid,self.serverqueue).start()
		
	def emailchat(self,chatsessionid,emailaddress):
		email_values={'_m':'livesupport',
		'_a':'emailchat',
		'chatsessionid':chatsessionid,
		'utf8':'1',
		'emailaddress':emailaddress,
		'sessionid':self.sessionid}
		email_request=createrequest(self.session_url,email_values)
		getserverresponse(email_request,self.lrbrowser,'emailchat',chatsessionid,self.serverqueue).start()
		
		
	def gethistory(self,visitorsessionid):
		history_request=createrequest(self.session_url+
		'&_m=livesupport&_a=visitorhistory&utf8=1'+
		'&visitorsessionid='+visitorsessionid+
		'&sessionid='+self.sessionid)
		
		##History feature not implemented in LR Window therfore returning a URL
		return self.session_url+\
		'&_m=livesupport&_a=visitorhistory&utf8=1'+\
		'&visitorsessionid='+visitorsessionid+\
		'&sessionid='+self.sessionid
		#getserverresponse(history_request,self.lrbrowser,'visitorhistory'+chatsessionid,self.serverqueue).start()
		
	def transferchat(self,chatsessionid,transfertoid):
		transfer_values={'_m':'livesupport',
		'_a':'transferchat',
		'chatsessionid':chatsessionid,
		'utf8':'1',
		'totransfer':transfertoid,
		'sessionid':self.sessionid}
		transfer_request=createrequest(self.session_url,transfer_values)
		getserverresponse(transfer_request,self.lrbrowser,'transferchat',chatsessionid,self.serverqueue).start()
	
	def pushpagevisitor(self,chatsessionid,url):
		pushpage_values={'_m':'livesupport',
		'_a':'pushpagevisitor',
		'chatsessionid':chatsessionid,
		'utf8':'1',
		'url':url,
		'sessionid':self.sessionid}
		pushpage_request=createrequest(self.session_url,pushpage_values)
		getserverresponse(pushpage_request,self.lrbrowser,'pushpage',chatsessionid,self.serverqueue).start()
		
	def pushimagevisitor(self,chatsessionid,url):
		pushimage_values={'_m':'livesupport',
		'_a':'pushimagevisitor',
		'chatsessionid':chatsessionid,
		'utf8':'1',
		'url':url,
		'sessionid':self.sessionid}
		pushimage_request=createrequest(self.session_url,pushimage_values)
		getserverresponse(pushimage_request,self.lrbrowser,'pushimage',chatsessionid,self.serverqueue).start()
		
	def requestchat(self,visitorsessionid):
		requestchat_values={'_m':'livesupport',
		'_a':'proactiverequestchat',
		'visitorsessionid':visitorsessionid,
		'utf8':'1',
		'sessionid':self.sessionid}
		requestchat_request=createrequest(self.session_url,requestchat_values)
		getserverresponse(requestchat_request,self.lrbrowser,'requestchat',visitorsessionid,self.serverqueue).start()
		
	def forcechat(self,visitorsessionid):
		requestchat_values={'_m':'livesupport',
		'_a':'proactiverequestchat',
		'visitorsessionid':visitorsessionid,
		'utf8':'1',
		'sessionid':self.sessionid}
		forcechat_request=createrequest(self.session_url,forcechat_values)
		getserverresponse(forcechat_request,self.lrbrowser,'forcechat',visitorsessionid,self.serverqueue).start()
	
	def getchatstatus(self,visitorsessionid):
		chatstatus_request=createrequest(self.session_url+
		'&_m=livesupport&_a=visitorchatstatus&utf8=1'+
		'&visitorsessionid='+visitorsessionid+
		'&sessionid='+self.sessionid)
		getserverresponse(chatstatus_request,self.lrbrowser,'chatstatus',visitorsessionid,self.serverqueue).start()
		
	def refreshchat(self,chaturl,chatsessionid):
		refresh_request=createrequest(self.product_url+'winapp/index.php'+chaturl)
		getserverresponse(refresh_request,self.lrbrowser,'chatrefresh',chatsessionid,self.serverqueue).start()
