#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#此文件主要用于：
#1、运行所有以Test开头的测试用例文件,即：一次执行所有测试用例:test_*.py
#2、生成测试报告，格式为：当天日期+时间_result.html
#3、定义测试报告的存放的相对路径

import unittest
from public import HTMLTestRunner
import time
import os

casepath = ".\\TestCase\\"
result = ".\\result\\"


def Creatsuite():
	#定义单元测试容器
	testunit = unittest.TestSuite()

	#定搜索用例文件的方法
	discover = unittest.defaultTestLoader.discover(casepath, pattern='test_*.py', top_level_dir=None)

	#将测试用例加入测试容器中
	for test_suite in discover:
		for casename in test_suite:
			testunit.addTest(casename)
		print testunit
	return testunit

#声明用例集合
test_case = Creatsuite()

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

#定义单个测试报告的存放路径，支持相对路径
tdresult = result + day
#存在以当天日期为名称的文件夹的情况，则……
if os.path.exists(tdresult):
	filename = tdresult + "\\" + now + "_result.html"
	fp = file(filename, 'wb')
	#定义测试报告
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')

	#运行测试用例
	runner.run(test_case)
	fp.close()  #关闭报告文件
else:
	#不存在以当天日期为名称的文件夹的情况，则……
	os.mkdir(tdresult)
	filename = tdresult + "\\" + now + "_result.html"
	fp = file(filename, 'wb')
	#定义测试报告
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')

	#运行测试用例
	runner.run(test_case)
	fp.close()  #关闭报告文件