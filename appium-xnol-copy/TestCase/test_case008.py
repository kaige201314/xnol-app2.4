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
#引入PageObject下的financePage
from PageObject import financePage
from PageObject.financePage import FinancePage

#test_case008:登录——》提取天天牛、月月牛——》退出

#提取天天牛、月月牛的账户，必须是有可提取金额的账户
username='christy'
password='123456'
 

class test_case008(unittest.TestCase,loginPage.LoginPage):
 
    
    def setUp(self):
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', BasePage.BaseAction.capabilities)
    
    
    #登录+提取天天牛+提取月月牛
    def test_extract(self):
        u'''提取月月牛+提取天天牛'''
        loginPage.LoginPage(self.driver).userLogin(username,password)
        #提取月月牛
        myPage.MyPage(self.driver).smart_interest_extract()
        #提取天天牛
        myPage.MyPage(self.driver).current_interest_extract()
        #退出
        loginPage.LoginPage(self.driver).userlogout()
 
     
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

    
