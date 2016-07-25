#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import unittest
from appium import webdriver

#引用别的目录中的模块
sys.path.append("..")
#引入PageObject下的BasePage
from PageObject import BasePage
#引入PageObject下的loginPage
from PageObject import loginPage
from PageObject.loginPage import LoginPage
#引入PageObject下的myPage
from PageObject import myPage
from PageObject.myPage import MyPage
#引入PageObject下的accountPage
from PageObject import accountPage
from PageObject.accountPage import AccountPage
#引入Public下的read_from_phoneNO
from Public import read_from_phoneNO
from Public.read_from_phoneNO import Read_from_phoneNO
#引入读取函数
from Public import read_from_txt
from Public.read_from_txt import Read_from

#test_case002：登录——》设置交易密码——》退出



class test_case002(unittest.TestCase,loginPage.LoginPage):
 
    
    def setUp(self):
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', BasePage.BaseAction.capabilities) 
    
    
    #登录+设置交易密码+退出
    def test_tradeCode(self):
        u'''设置交易密码'''
        #读取刚刚注册的新用户的用户名
        username=read_from_phoneNO.Read_from_phoneNO().read_phoneNO()
        password=read_from_txt.Read_from().read_from('login_password.txt') 
        #登录
        loginPage.LoginPage(self.driver).userLogin(username,password)
        #设置交易密码
        accountPage.AccountPage(self.driver).set_tradeCode(username)
        #退出
        loginPage.LoginPage(self.driver).userlogout()

 
     
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

    
