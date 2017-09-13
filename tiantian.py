# -*- coding: UTF-8 -*-
import requests
import itchat
from itchat.content import *
import sys  
import json
import time
from time import sleep
import settings
from xiaozhushou_util.xiaozhushou_util import *
import re
reload(sys)  
sys.setdefaultencoding('utf8')

itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.get_chatrooms(update=True)
settings.init()

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(settings.vT, msg['RecommendInfo']['UserName'])

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
  CurUserName = msg['FromUserName']
  if(u'管理猿加密码' in msg['Content']):
    settings.admins.append(CurUserName)  
    itchat.send_msg(u'您已是管理猿',CurUserName)
  sendGroupInviteMsg(msg,CurUserName)

#send group invite msg according to digits
def sendGroupInviteMsg(msg,CurUserName):
  msgText = msg['Text']
  x = re.findall(r'\d+', msgText)
  #print x
  if(len(x) >0):
    y= int(x[0])
    if(y>=0 and y<=10):
      #print settings.chatGroups[y]
      if(preventAbuseTalking(CurUserName)):
        return
      pullMembersMore(msg, settings.chatGroups[y], CurUserName)
      sleep(0.5)
    elif(y==99):
      advertiseQR(CurUserName)
  itchat.send_msg(settings.vT, CurUserName)
  sleep(0.5)
  msgText = msg['Text']

#if group chat msg contains kick ads, start kicking logic
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
  if msg['ActualUserName'] in settings.admins:
    content = msg['Content']
    if(content[0]=="@"):
      if u'广告' in content:
        delUser(msg['FromUserName'],content,settings.ADMIN)

itchat.run() 

