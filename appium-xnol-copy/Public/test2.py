#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

mobileNo='13066889188'

import os

p='PageObject/phoneNO.txt'
#获取当前文件的绝对路径
print os.path.abspath(os.path.dirname(__file__))
#获取当前文件的绝对路径，然后拼接P
print os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,p))
