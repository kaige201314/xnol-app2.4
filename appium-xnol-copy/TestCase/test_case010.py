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

#test_case0010:登录——》购买VIP专享标——》退出

username='xnwa1244598'
password='123456'


class test_case010(unittest.TestCase,loginPage.LoginPage):
 
    
    def setUp(self):
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', BasePage.BaseAction.capabilities)

    
    
    #登录+购买VIP专享标
    def test_Buy_current_smart(self):
        u'''购买VIP专享标'''
        #登录
        loginPage.LoginPage(self.driver).userLogin(username,password)
                
        #购买VIP专享标
        financePage.FinancePage(self.driver).buy_VIP_exclusive_prpject()
        
        #退出
        loginPage.LoginPage(self.driver).userlogout()
        
 
     
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

    
