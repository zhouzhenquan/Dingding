"""
-- coding: utf-8 --
@Time : 2020/8/6 19:36
@Author : 周振全
@Site : 
@File : Screenshot.py
@Software: PyCharm

"""
import os

def screenshot():
    img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path=img_folder+"下班"+'.png'
    return  path
