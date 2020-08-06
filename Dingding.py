"""
-- coding: utf-8 --
@Time : 2020/8/5 14:17
@Author : 周振全
@Site :
@File : Dingding.py
@Software: PyCharm

"""

"""
钉钉下班打卡
"""
import os
from appium import webdriver
import time
import Screenshot




def Ma():
    # 在什么系统上操作
    desired_caps = {}
    desired_caps["platformName"] = "Android"
    desired_caps["platformVersion"] = 8.0
    desired_caps["deviceName"] = "Android Emulator"
    desired_caps["appPackage"] = "com.alibaba.android.rimet"
    desired_caps["appActivity"] = "com.alibaba.android.rimet.biz.LaunchHomeActivity"
    desired_caps["noReset"] = True
    # 连接appium服务器
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.implicitly_wait(10)
    driver.find_element_by_id("com.alibaba.android.rimet:id/home_bottom_tab_button_work").click()
    time.sleep(10)
    a1 = 135/1069
    b1 = 1400/1916
    # 获取当前手机屏幕大小X,Y
    X = driver.get_window_size()['width']
    Y = driver.get_window_size()['height']
    # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
    driver.tap([(a1*X, b1*Y)])

    a1 = 530/1069
    b1 = 1200/1916
    # 获取当前手机屏幕大小X,Y
    X = driver.get_window_size()['width']
    Y = driver.get_window_size()['height']
    # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
    time.sleep(30)
    driver.tap([(a1*X, b1*Y)])

    time.sleep(5)
    print('开始截图')
    driver.get_screenshot_as_file(Screenshot.screenshot())
    print('截图结束')

