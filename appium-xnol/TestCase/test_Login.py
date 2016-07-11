#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import unittest
import time
from time import sleep
import BasePage
from BasePage import BaseAction
from PageObject import DashPage
from appium.webdriver.common.touch_action import TouchAction


class login(unittest.TestCase):
    
    def setup(self):
        pass
    
    #进入我的页面
    getMyPage=self.driver.by_xpath("//android.widget.CheckBox[contains(@text,'我的')]")
    
    #获取未登录时我的页面的账户状态
    getAccountWithNoLogin=driver.by_id("com.xiaoniu.finance:id/account_no_login")
        
    #点击“登录”，进入登录页面
    def click_login(self):
        #首先返回到"我的"页面
        #Dash(driver).recover()
        sleep(4)
        self.getMyPage.click()
        self.getAccountWithNoLogin.click()
        sleep(2)
    
    #定位用户名输入框
    username=driver.by_class_names("android.widget.EditText")[0]
    #定位密码输入框
    password=driver.by_class_names("android.widget.EditText")[1]
    
    #定位登录框，先清理一下，再输入用户名
    def input_userName(self,username):
        self.username.clear()
        self.username.send_keys(username)
        
    #定位登录框，输入密码
    def input_passWord(self,password):
        self.password.send_keys(password)
    
    #定位登录按钮
    loginButton=driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'登录')]")
       
    #点击登录按钮
    def click_loginButton(self):
        self.loginButton.click()
     
    #判断登录是否成功
    def judgeLoginOrNot(self,accountName):
        try:
            WebDriverWait(self.driver,60).until(EC.visibility_of_element_located((By.NAME,accountName)))
            print '%s——>登录成功!' %(accountName)
        except:
            print '%s——>登录失败！' %(accountName)
                
  
    #封装登录方法
    def userLogin(self,username,password):
        self.click_login()
        self.input_userName(username)
        self.input_passWord(password)
        self.click_loginButton()
              
        
    
    
    #登录测试    
    def test_login(self):
        self.userLogin('panbishi',123456)
        #指定账户名称，判断登录是否成功
        self.judgeLoginOrNot('邱君华') 
    
    
    def tearDown(self):
        pass



