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

#test_case009:登录——》添加理财金券——》购买天天牛——》购买月月牛——》购买安心牛——》购买散标——》购买富盈人生——》购买理财金体验标——》退出

username='13066889001'
password='a1234567'


class test_case009(unittest.TestCase,loginPage.LoginPage):
 
    
    def setUp(self):
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', BasePage.BaseAction.capabilities)

    
    
    #登录+购买天天牛
    def test_Buy_products(self):
        u'''购买各类产品标的'''
        #登录
        loginPage.LoginPage(self.driver).userLogin(username,password)
        
        #添加理财金券
        myPage.MyPage(self.driver).add_financial_coupons_function()
        
        #先定位到理财页，再进入项目分类页面
        financePage.FinancePage(self.driver).finance_to_projectType()
       
        #购买天天牛
        financePage.FinancePage(self.driver).buy_current_interest_project()
        
        #购买月月牛
        financePage.FinancePage(self.driver).buy_smart_interest_project()
        
        #购买安心牛
        financePage.FinancePage(self.driver).buy_optimiz_interest_project()
        
        #购买散标
        financePage.FinancePage(self.driver).buy_scattered_interest_project()
        
        #购买富盈人生
        financePage.FinancePage(self.driver).buy_fuying_life_interest_project()
            
        #购买理财金体验标
        financePage.FinancePage(self.driver).buy_financial_experience_project()
        
        #退出
        loginPage.LoginPage(self.driver).userlogout()
            
                
     
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

    
