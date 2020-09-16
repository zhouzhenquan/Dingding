"""
-- coding: utf-8 --
@Time : 2020/8/6 16:17
@Author : 周振全
@Site : 
@File : Run_XiaBan.py
@Software: PyCharm

"""
import os
import Dingding
import datetime
from Email import send_email


def special():
    # 启动appium服务器
    os.system('startAppiumServer.bat')
    Dingding.Ma()
    i = datetime.datetime.now().strftime("%p")
    S = "PM"
    if i == S:
        send_email("【  下班打卡  】 ")
    else:
        send_email("【  上班打卡  】")
special()
