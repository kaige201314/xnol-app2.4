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




username='18954884354'
password='a12345678'   

class test_xxk_practice(unittest.TestCase,loginPage.LoginPage):
 
    
    def setUp(self):
        pass
    
    
    #登录+退出
    def test_BingdingRecharge(self):
        loginPage.LoginPage().userLogin(username,password)
        myPage.MyPage().click_myPage_recharge_Button()
        myPage.MyPage().input_rechargeValue()
        myPage.MyPage().choose_item_bank_check()
        myPage.MyPage().click_recharge_Button()
        myPage.MyPage().print_input_Areas()
 
     
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

    