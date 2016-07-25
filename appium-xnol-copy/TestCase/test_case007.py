#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')



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


#test_case007:登录——》设置——》修改——》关闭手势密码——》退出

class test_case007(unittest.TestCase,loginPage.LoginPage):
 
    
    def setUp(self):
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', BasePage.BaseAction.capabilities)

    
    
    #登录+设置+修改+关闭手势密码+退出
    def test_Gesture(self):
        u'''设置+修改+关闭手势密码'''
        #读取刚刚注册的新用户的用户名
        username=read_from_phoneNO.Read_from_phoneNO().read_phoneNO()
        password='a12345678'
        loginPage.LoginPage(self.driver).userLogin(username,password)
        #设置手势密码
        accountPage.AccountPage(self.driver).set_userGesture()
        #修改手势密码
        accountPage.AccountPage(self.driver).change_userGesture()
        #关闭手势密码
        accountPage.AccountPage(self.driver).close_userGesture()
        #退出
        loginPage.LoginPage(self.driver).userlogout()

 
     
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

    
