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
#引入读取函数
from Public import read_from_txt
from Public.read_from_txt import Read_from
#引入Public下的read_from_phoneNO
from Public import read_from_phoneNO
from Public.read_from_phoneNO import Read_from_phoneNO

#test_case012:登录——》修改登录密码——》退出




class test_case012(unittest.TestCase,loginPage.LoginPage):
 
    
    def setUp(self):
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', BasePage.BaseAction.capabilities)

    
    
    #登录+修改登录密码
    def test_change_loginPassword(self):
        u'''修改登录密码'''
        #登录，使用前面用例test_case001注册的用户
        username=read_from_phoneNO.Read_from_phoneNO().read_phoneNO()
        password=read_from_txt.Read_from().read_from('login_password.txt')  
        loginPage.LoginPage(self.driver).userLogin(username,password)
        #修改登录密码，不需要退出操作
        accountPage.AccountPage(self.driver).change_loginPassword()



 
     
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

    
