# -*- coding: UTF-8 -*-
import requests
import itchat
from itchat.content import *
import sys
import json
import time
import xiaozhushou_util
from time import sleep
reload(sys)
sys.setdefaultencoding('utf8')

def getName(chatroomName):
    itchat.get_chatrooms(update=True)
    cur_chatrooms = itchat.search_chatrooms(name=chatroomName)
    detailedChatroom = itchat.update_chatroom(cur_chatrooms[0]['UserName'], detailedMember=True)
    #print(json.dumps(cur_chatrooms)+"\n")
    return detailedChatroom["UserName"]
def get_response(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : '8028064e9e2f46c78a111276823f94b1',
        'info'   : msg,
        'userid' : 'superchaoran',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return msg
def pullMembersMore(msg, chatroomName, CurUserName):
    cur_chatrooms = itchat.search_chatrooms(name=chatroomName)
    #print(json.dumps(cur_chatrooms)+"\n")
    chatRoomUserName = cur_chatrooms[0]['UserName']
    #print(chatRoomUserName + "\n")
    #print(CurUserName+ "\n")
    r = itchat.add_member_into_chatroom(chatRoomUserName,[{'UserName':CurUserName}],useInvitation=True)
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if u'超然' in msg['ActualNickName']:
      content = msg['Content']
      if(content[0]=="@"):
        if u'广告' in content:
          delUser(msg['FromUserName'],content)
#don't use, may hurt account
def delFromAllGroup(content):
  for i in range(len(chatGroups)):
    delUser(getName(chatGroups[i]),content)
def delUser(roomId, content):
  ret = itchat.delete_member_from_chatroom(roomId,[{'UserName':searchUser(getChatroomMemberList(roomId),content)}])
  if(ret):
    itchat.send('为保持群内清洁,已清除广告号~😊',toUserName=roomId)
def searchUser(users,target):
  for user in users:
    if( (user['NickName']!='' and user['NickName'] in target) or ((user['DisplayName']!='') and (user['DisplayName'] in target))):
        #or ((user['ActualNickName']!='') and (user['ActualNickName'] in target)))
      return user['UserName']
def getChatroomMemberList(roomId):
    itchat.get_chatrooms(update=True)
    detailedChatroom = itchat.update_chatroom(roomId, detailedMember=True)
    return detailedChatroom['MemberList']
