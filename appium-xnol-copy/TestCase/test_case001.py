#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')



import unittest
from appium import webdriver
from time import sleep

sys.path.append("..")
#引入PageObject下的myDriver
from PageObject import myDriver
from PageObject.myDriver import MyDriver
#引入PageObject下的BasePage
from PageObject import BasePage
from PageObject.BasePage import BaseAction 
#引入PageObject下的loginPage
from PageObject import loginPage
from PageObject.loginPage import LoginPage
#引入PageObject下的accountPage
from PageObject import accountPage
from PageObject.accountPage import AccountPage


#：test_case001：新用户注册——》关闭手势密码——》退出

class test_case001(unittest.TestCase,loginPage.LoginPage):
    

    
    def setUp(self):
        self.driver=self.driver=webdriver.Remote('http://localhost:4723/wd/hub', BasePage.BaseAction.capabilities) 

    
    
    #注册+关闭手势密码+退出
    def test_Register(self):
        u'''注册新用户+注册后关闭手势密码'''
        #注册新用户，不需要登录，故而直接跳转到登录页面——》注册新用户
        loginPage.LoginPage(self.driver).user_Register()
        #关闭手势密码
        accountPage.AccountPage(self.driver).close_Rgesture_after_Register()
        #退出
        loginPage.LoginPage(self.driver).userlogout()
     
     
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

    