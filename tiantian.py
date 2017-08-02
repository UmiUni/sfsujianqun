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
freq = {}
usersDict = {}
itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.get_chatrooms(update=True)

chatGroups =[ 
u"天天刷题",
u"SFSU 三番桌游",
u"SFSU 租房",
u'SFSU 三番拼车',
u'SFSU 三番校友',
u'SFSU 三番美食',
u'SFSU 三番二手',
u'北美CPA',
u'线上KTV',
u'北美信用卡',
u'小助手测试群0',
u'小助手测试群1'
] 

v0= u"您好,SFSU三番加群建群小助手为您服务:)\n"
v1= u"回复 0 加CS刷题、竞赛、面试;\n"
v2= u"回复 1 SFSU三番桌游群\n"
v3= u"回复 2 加SFSU三番租房群;\n"
v4= u"回复 3 加SFSU三番拼车群;\n"
v5= u"回复 4 加SFSU三番校友群;\n"
v6= u"回复 5 加SFSU三番美食约饭群;\n"
v7= u"回复 6 加SFSU三番二手货群;\n"
v8= u"回复 7 加北美CPA,REG天天刷题群;\n"
v9= u"回复 8 加线上KTV开嗓🎙️北美总群\n"
v10= u"回复 9 加北美信用卡爱好者总群\n"
vT =v0+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10

@itchat.msg_register('Friends')
def add_friend(msg):
    #print("add message:")
    #print(json.dumps(msg))
    #msg.user.verify()
    #itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.add_friend(**msg['Text'])
    #itchat.add_friend(userName = msg['RecommendInfo']['UserName'], status=3, verifyContent=u'UIUC万群汇总', autoUpdate=True)
    #msg.user.send(vT)
    #response = itchat.add_friend(userName = CurUserName, status=3, autoUpdate=True)
    itchat.send_msg(vT, msg['RecommendInfo']['UserName'])

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
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    CurUserName = msg['FromUserName']
    #print(json.dumps(response)+"\n")
    print("userid:"+CurUserName+"\n") 
    if(CurUserName in usersDict):
        usersDict[CurUserName] = usersDict[CurUserName] + 1
        if(usersDict[CurUserName] >= 10):
            itchat.send_msg(u'您已达到今日加群上限，请明日再来～😊', CurUserName)
            return
    else:
        usersDict[CurUserName] = 1
    msgText = msg['Text']
    for x in range (0, 10):
      if(str(x) in msgText):
        pullMembersMore(msg, chatGroups[x], CurUserName)
        sleep(0.5)
    itchat.send_msg(vT, CurUserName)
    sleep(0.5)

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if u'超然' in msg['ActualNickName']:
      content = msg['Content']
      if(content[0]=="@"):
        if u'广告' in content:
          delUser(msg['FromUserName'],content)

itchat.run() 
