# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :Dingding_Test
# @File     :TTime
# @Date     :2020/8/13 14:40
# @Author   :周振全
# @Email    :1275470984
# @Software :PyCharm
-------------------------------------------------
"""
import time
import datetime

def Time_Week():
    # 今天星期几
    dict = {1: "星期一", 2: "星期二", 3: "星期三", 4: "星期四", 5: "星期五", 6: "星期六", 0: "星期天"}
    # 今天是几年几月几号
    now_time = datetime.datetime.now()

    Year = now_time.year    # 年
    Month = now_time.month  # 月
    Day = now_time.day      # 日

    Weekday = dict.get(int(time.strftime("%w")))  # 获取星期几
    Minute_Second_Weekday = time.strftime("%H:%M:%S",time.localtime(time.time()))   #获取 时：分：秒
    SUM = ("{}年{}月{}日   {}   {} ".format(Year, Month, Day,Weekday, Minute_Second_Weekday))
    return SUM

