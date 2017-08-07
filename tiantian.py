# -*- coding: UTF-8 -*-
import requests
import itchat
from itchat.content import *
import sys  
import json
import time
from time import sleep
import settings
from xiaozhushou_util import *
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
  if(preventAbuseTalking(CurUserName)):
    return
  sendGroupInviteMsg(msg,CurUserName)

#send group invite msg according to digits
def sendGroupInviteMsg(msg,CurUserName):
  msgText = msg['Text']
  x = re.findall(r'\d+', msgText)
  #print x
  if(len(x) >0):
    y= int(x[0])
    if(y>=0 and y<=9):
      #print settings.chatGroups[y]
      pullMembersMore(msg, settings.chatGroups[y], CurUserName)
      sleep(0.5)
  itchat.send_msg(settings.vT, CurUserName)
  sleep(0.5)
  msgText = msg['Text']

#if group chat msg contains kick ads, start kicking logic
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    #if msg['ActualNickName'] in settings.admins:
    if msg['ActualUserName'] in settings.admins:
      content = msg['Content']
      if(content[0]=="@"):
        if u'广告' in content:
          delUser(msg['FromUserName'],content)

itchat.run() 

