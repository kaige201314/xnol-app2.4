#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import unittest
from PageObject import BasePage
from PageObject import loginPage
from PageObject.loginPage import LoginPage
from appium import webdriver
from time import sleep


#：test_case001——》注册

username='panbishi'
password=123456   

class test_case001(unittest.TestCase,loginPage.LoginPage):

 
    
    def setUp(self):
        pass


    
    #登录测试
    def test_login(self):
        loginPage = LoginPage('http://localhost:4723/wd/hub', BasePage.BaseAction.capabilities)
        loginPage.userLogin(username,password)
        loginPage.judgeLoginOrNot('邱君华')
        

        
    def tearDown(self):
        pass
   



if __name__ == '__main__':
    unittest.main()

    