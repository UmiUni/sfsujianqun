# -*- coding: UTF-8 -*-
import datetime
def init():

  global chatGroups
  global vT
  global usersDict
  global admins
  global ADMIN
  global previousDay 

  chatGroups =[
  u"leetcode天天",
  u"SFSU三番活动",
  u"SFSU三番租房",
  u'SFSU三番拼车',
  u'SFSU三番内推',
  u'SFSU三番美食',
  u'SFSU三番二手',
  u'北美CPA',
  u'线上KTV',
  u'北美信用卡',
  u'北美表情分享',
  u'北美游戏交流',
  u'Chuck郭律师',
  ]

  v0= u"您好,SFSU三番加群建群小助手为您服务:)\n"
  v00=u"每天只能加3个群哦;\n"
  v1= u"回复 0 加CS刷题、竞赛、面试;\n"
  v2= u"回复 1 SFSU三番活动群\n"
  v3= u"回复 2 加SFSU三番租房群;\n"
  v4= u"回复 3 加SFSU三番拼车群;\n"
  v5= u"回复 4 加SFSU三番内推找工作群;\n"
  v6= u"回复 5 加SFSU三番美食约饭群;\n"
  v7= u"回复 6 加SFSU三番二手货群;\n"
  v8= u"回复 7 加北美CPA,REG天天刷题群;\n"
  v9= u"回复 8 加线上KTV开嗓🎙️北美总群\n"
  v10= u"回复 9 加北美信用卡爱好者总群\n"
  v11= u"回复 10 加北美表情分享总群\n"
  v12= u"回复 11 加北美游戏交流总群\n"
  v13= u"回复 12 加Chuck郭律师美帝绿卡讨论群.\n"
  v14= u"回复 99 查看【北美加群小助手Jogchat.com】微信公众号二维码加硅谷、纽约、西雅图、UIUC、Purdue等群\n"
  vT =v0+v00+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14
  usersDict = {}
  admins=[] 
  ADMIN = u'SFSU三番加群小助手'
  previousDay = datetime.datetime.now().day
