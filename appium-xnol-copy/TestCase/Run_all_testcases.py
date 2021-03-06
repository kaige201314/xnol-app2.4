#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#此文件主要用于：
#1、运行所有以Test开头的测试用例文件,即：一次执行所有测试用例:test_*.py
#2、生成测试报告，格式为：当天日期+时间_result.html
#3、定义测试报告的存放的相对路径

import unittest
import time
import os
#引用别的目录中的模块
sys.path.append("..")
from Public import HTMLTestRunner

casepath = "..\\TestCase\\"
result = "..\\result\\"


def CreatSuite():
	#定义单元测试容器
	suite=unittest.TestSuite()
	#定搜索用例文件的方法
	discover=unittest.defaultTestLoader.discover(casepath, pattern='test_*.py', top_level_dir=None)
	#将discover方法筛选出来的用例，循环添加到测试套件中,打印出的用例信息会递增
	for test_case in discover:
			suite.addTests(test_case)
			
	print suite			
	return suite



if __name__ == "__main__":
	#所有的用例集合
	all_test_cases = CreatSuite()

	#获取系统当前时间
	now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
	day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

	#定义单个测试报告的存放路径，支持相对路径
	tdresult = result + day
	
	#若已经存在以当天日期为名称的文件夹的情况，则直接将测试报告放到这个文件夹之下
	if os.path.exists(tdresult):
		filename = tdresult + "\\" + now + "_result.html"
		#以写文本文件或写二进制文件的模式打开测试报告文件
		fp = file(filename, 'wb')
		#定义测试报告
		runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'小牛在线APP2.4.0-UI自动化测试报告', description=u'用例执行情况如下：')
		#运行测试用例
		runner.run(all_test_cases)
		#关闭报告文件
		fp.close()
	else:
		#不存在以当天日期为名称的文件夹的情况，则建立一个以当天日期为名称的文件夹
		os.mkdir(tdresult)
		#以写文本文件或写二进制文件的模式打开测试报告文件
		filename = tdresult + "\\" + now + "_result.html"
		fp = file(filename, 'wb')
		#定义测试报告
		runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'小牛在线APP2.4.0-UI自动化测试报告', description=u'用例执行情况如下：')
		#运行测试用例
		runner.run(all_test_cases)
		#关闭报告文件
		fp.close()