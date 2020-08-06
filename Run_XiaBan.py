"""
-- coding: utf-8 --
@Time : 2020/8/6 16:17
@Author : 周振全
@Site : 
@File : Run_XiaBan.py
@Software: PyCharm

"""
import Dingding
from Email import send_email

def special():
        Dingding.Ma()
        send_email("【下班】 打卡 ！！！")
special()