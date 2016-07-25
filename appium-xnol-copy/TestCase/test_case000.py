#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import unittest
sys.path.append("..")
#引入PageObject下的myDriver
from PageObject import myDriver
from PageObject.myDriver import MyDriver

from PageObject import BasePage
from PageObject import loginPage
from PageObject.loginPage import LoginPage
from appium import webdriver
from time import sleep


#：test_case000：老用户登录——》退出
#用户的用户名和密码《————登录方法userlogin()会用到的参数
username='panbishi'
password='123456'   



class test_case000(unittest.TestCase,loginPage.LoginPage):
        
 
    
    def setUp(self):
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', BasePage.BaseAction.capabilities) 
    
    
    #登录+退出
    def test_login(self):
        u'''老用户登录——》退出'''
        loginPage.LoginPage(self.driver).userLogin(username,password)
        loginPage.LoginPage(self.driver).userlogout()

  
     
    def tearDown(self):
        self.driver.quit()
        
        
        



if __name__ == '__main__':
    unittest.main()

    