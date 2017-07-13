# -*- coding: UTF-8 -*-
import requests
import itchat
from itchat.content import *
import sys  
import json
import time
from time import sleep
reload(sys)  
sys.setdefaultencoding('utf8')
freq = {}
usersDict = {}
itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.get_chatrooms(update=True)

v0= u"您好,SFSU三番加群建群小助手为您服务:)\n"
v1= u"回复 1 加CS刷题、竞赛、面试;\n"
v2= u"回复 2 SFSU三番桌游群\n"
v3= u"回复 3 加SFSU三番租房群;\n"
v4= u"回复 4 加SFSU三番拼车群;\n"
v5= u"回复 5 加SFSU三番校友群;\n"
v6= u"回复 6 加SFSU三番美食约饭群;\n"
v7= u"回复 7 加SFSU三番二手货群;\n"
v8= u"回复 8 加北美CPA,REG天天刷题群;\n"
v9= u"回复 9 加线上KTV开嗓🎙️北美总群\n"
v10= u"回复 9 加北美信用卡爱好者总群\n"
vT =v0+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10
#Chaoran userid:@ef633e828340000b5518a18f66daefbf8f307a1fa96d405288a885014d8c25d5
#汪灵欣 userid:@eb21513f32b62cd9773abc2fd5531ee05ca09af4ca926fbf896d8c89f29e46cc
#groups= {'@@6cdcfcb7dc00e7d546464ba702151143e1bf4aa9f72aa6e2559b86469e9a2481':'天天VIP','@@0515f86f31ec80ce4d4238a9ada8fdc0dd0900cc017f87c17df8ee49fb6d4663':'雷孙王'}
#groups= {'@@d8b03e5ed3d34267d563c552a33af7b975e7375dd0a0499965292b2621fdee40':'万能总群2','@@8bd479db2f43c6e2bf8ba14caf6cb2297dd0bf66235e88760457ef9d2d323dd2':'万能总群3'}
# 收到好友邀请自动添加好友

def getName(chatroomName):
    itchat.get_chatrooms(update=True)
    cur_chatrooms = itchat.search_chatrooms(name=chatroomName)
    detailedChatroom = itchat.update_chatroom(cur_chatrooms[0]['UserName'], detailedMember=True)
    #print(json.dumps(cur_chatrooms)+"\n")
    return detailedChatroom["UserName"]

'''
groups={}
#groups[getName(u'天天VIP')] = u'天天VIP'
#groups[getName(u'雷孙王')] = u'雷孙王'
#groups[getName(u'UIUC 万能总群2')] = u'万能总群2'
#groups[getName(u'UIUC 万能总群3')] = u'万能总群3'
groups[getName(u'UI食神带飞')] = u'UI食神带飞'
groups[getName(u'Stanford湾区饮食')] = u'Stanford湾区饮食'
#groups={}
#groups[getName(u'天天VIP')] = u'天天VIP'
#groups[getName(u'雷孙王')] = u'雷孙王'
#groups[getName(u'UIUC 万能总群2')] = u'万能总群2'
#groups[getName(u'UIUC 万能总群3')] = u'万能总群3'
#groups[getName(u'UIUC CS刷题小分队')] = u'UIUC刷题小分队'
#groups[getName(u'天天刷题')] = u'天天刷题'
'''
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
#"ChatRoomOwner": "@cb680fd93595dafaaeb9c915e08c8d0c6ec5878f4a8e33612ab0ba95c2dc3992"
# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
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
    if "1" in msgText and ("10" not in msgText):
        pullMembersMore(msg, u'天天刷题', CurUserName)
        sleep(0.5)
    elif "2" in msgText:
        pullMembersMore(msg, u'SFSU 三番桌游群', CurUserName)
        sleep(0.5)
    elif "3" in msgText:
        pullMembersMore(msg, u'SFSU 租房', CurUserName)
        sleep(0.5)
    elif "4" in msgText:
        pullMembersMore(msg, u'SFSU 三番拼车', CurUserName)
        sleep(0.5)
    elif "5" in msgText:
        pullMembersMore(msg, u'SFSU 三番校友', CurUserName)
        sleep(0.5)
    elif "6" in msgText:
        pullMembersMore(msg, u'SFSU 三番美食', CurUserName)
        sleep(0.5)
    elif "7" in msgText:
        pullMembersMore(msg, u'SFSU 三番二手', CurUserName)
        sleep(0.5)
    elif "8" in msgText:
        pullMembersMore(msg, u'北美CPA', CurUserName)
        sleep(0.5)
    elif "9" in msgText:
        pullMembersMore(msg, u'线上KTV', CurUserName)
        sleep(0.5)
    elif "10" in msgText:
        pullMembersMore(msg, u'北美信用卡', CurUserName)
        sleep(0.5)
    else:
        itchat.send_msg(vT, CurUserName)
        sleep(0.5)

def pullMembersMore(msg, chatroomName, CurUserName):
    cur_chatrooms = itchat.search_chatrooms(name=chatroomName)
    #print(json.dumps(cur_chatrooms)+"\n")
    chatRoomUserName = cur_chatrooms[0]['UserName']
    #print(chatRoomUserName + "\n")
    #print(CurUserName+ "\n")
    r = itchat.add_member_into_chatroom(chatRoomUserName,[{'UserName':CurUserName}],useInvitation=True)

#@itchat.msg_register([TEXT, SHARING], isGroupChat=True)
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    msgS = msg.text
    '''
    print(msg['isAt'])
    print(msg['ActualNickName'])
    print(msg['Content'])
    '''
    if "@Stanford加群" in msg['Content']:
        replyS = get_response(msgS)
        if msg.actualNickName.count("@")>=2:
            msg.user.send(u'%s' % (replyS+'~想进群加我😊'))
        else:
            msg.user.send(u'@%s\u2005%s' % (msg.actualNickName, replyS+'~想进群加我😊'))
    '''  
    ###超级广告###
    if not msg.isAt:
        groudIDOrigin = msg['FromUserName']
        groudID = groudIDOrigin[:35]
        if groudID in freq:
            if(freq[groudID] % 20 == 5):
                print("groundID"+str(groudID)+ "\n")
                print("frequency"+ str(freq[groudID])+ "\n")
                freq[groudID] = freq[groudID] + 1
                #itchat.send('北美万群汇总，组建租房、二手货／车、健身、面试竞赛刷题、信用卡爱好者、美食、剁手、课程专业、实习工作群，群已超过万人，进群请加我😊', toUserName=groudIDOrigin)
                itchat.send('UIUC、北美万群汇总目录～进群请加我😊~',toUserName=groudIDOrigin)
            else:
                #print("groundID"+str(groudID)+ "\n")
                #print("frequency"+ str(freq[groudID])+ "\n")
                freq[groudID] = freq[groudID] + 1
        else:
            freq[groudID] = 1
            print("groundID"+str(groudID)+ "\n")
            print("frequency"+ str(freq[groudID])+ "\n")
    '''
        #if((' ' in msgS) == True):
        #msgS = msgS.split(' ', 1)[1]
        
        #print msgS
        #replyS = get_response(msgS) + ' ps:加我进群' 
        #msg.user.send(u'@%s\u2005I received: %s' % (msg.actualNickName, msg.text)
        #print("New Friend:"+ json.dumps(msg))
     
    '''
    if(1==1):
        source = msg['FromUserName']
        # 处理文本消息
        #print("source:"+source)
        if msg['Type'] == TEXT:
            # 消息来自于需要同步消息的群聊
            #print("prepare send0:")
            #print(json.dumps(groups))
            if source in groups:    
                #print("prepare send1:")            
                # 转发到其他需要同步消息的群聊
                #print(source)
                for item in groups.keys():
                    if not item == source:
                        # groups[source]: 消息来自于哪个群聊
                        # msg['ActualNickName']: 发送者的名称
                        # msg['Content']: 文本消息内容
                        # item: 需要被转发的群聊ID
                        #print("prepare send2:")
                        itchat.send('%s: %s:\n%s' % (groups[source], msg['ActualNickName'], msg['Content']), item)
        # 处理分享消息
        elif msg['Type'] == SHARING:
            if source in groups:
                for item in groups.keys():
                    if not item == source:
                        # msg['Text']: 分享的标题
                        # msg['Url']: 分享的链接
                        itchat.send('%s: %s:\n%s\n%s' % (groups[source], msg['ActualNickName'], msg['Text'], msg['Url']), item)
        
        '''

'''
# 处理图片和视频类消息
@itchat.msg_register([PICTURE, VIDEO], isGroupChat=True)
def group_reply_media(msg):
    source = msg['FromUserName']
    #print("source:"+source)
    # 下载图片或视频
    if source in groups:
        #print(source)
        msg['Text'](msg['FileName'])
        for item in groups.keys():
            if not item == source:
                # 将图片或视频发送到其他需要同步消息的群聊
                itchat.send('%s: %s:' % (groups[source], msg['ActualNickName']), item)
                itchat.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']), item)
                '''
'''
def updateChatroom(chatroomName):
    cur_chatrooms = itchat.search_chatrooms(name=u'UIUC租房3群')
    detailedChatroom = itchat.update_chatroom(cur_chatrooms[0]['UserName'], detailedMember=False)
    #print(json.dumps(detailedChatroom )+"\n")
'''



itchat.run() 
