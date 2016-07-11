#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#此文件主要用于：
#1、单步执行以Test开头的测试用例文件,即：一次执行添加到TestSuite()中的测试用例；
#2、生成测试报告，格式为：当天日期+时间_result.html;
#3、定义测试报告的存放的相对路径;

import unittest
import sys, time, os
import HTMLTestRunner
sys.path.append("TestCase")




from TestCase import test_case001


#定义测试用例存放路径，支持相对路径
case_path = ".\\TestCase\\"
#定义个报告存放路径，支持相对路径
result = ".\\Result\\"

def Creatsuite():
    #定义单元测试容器
    testunit = unittest.TestSuite()
    #定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_case001.py', top_level_dir=None)

    #将测试用例加入测试容器中
    for casename in discover:
        testunit.addTest(casename)
    print testunit
    return testunit



if __name__ == '__main__':
    test_case = Creatsuite()
    runner = unittest.TextTestRunner()
    runner.run(test_case)




