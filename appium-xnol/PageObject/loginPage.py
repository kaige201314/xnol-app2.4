#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import unittest
import time
from time import sleep
import BasePage
from BasePage import BaseAction
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#启动app
driver = webdriver.Remote('http://localhost:4723/wd/hub', BasePage.BaseAction.capabilities)
sleep(3)
    
class LoginPage(BasePage.BaseAction):

    #定位我的页面
    def getMyPage(self):
        #return self.by_xpath("//android.widget.CheckBox[contains(@text,'我的')]")
        return driver.find_element_by_name('我的')
    #定位用户头像（无论是否登录，头像的id不会变）
    def getAccount_header(self):
        return driver.by_id("com.xiaoniu.finance:id/account_header")
        
    #点击用户头像，进入登录页面（未登录）/用户信息页面（已登录）
    def click_headLogo(self):
        #首先返回到"我的"页面
        #Dash(driver).recover()
        sleep(3)
        self.getMyPage().click()
        self.getAccount_header().click()
        sleep(2)

#------------------------------------------------------------------------------------------------------------------------------------------------
    
    #定位用户名输入框
    def username(self):
        return self.by_class_names("android.widget.EditText")[0]
        
    #定位密码输入框
    def password(self):
        return self.by_class_names("android.widget.EditText")[1]
    
    #定位登录框，先清理一下，再输入用户名
    def input_userName(self,username):
        self.username().clear()
        self.username().send_keys(username)
        
    #定位登录框，输入密码
    def input_passWord(self,password):
        return self.password().send_keys(password)
    
    #定位登录按钮
    def loginButton(self):
        return self.by_xpath("//android.widget.Button[contains(@text,'登录')]")
       
    #点击登录按钮
    def click_loginButton(self):
        self.loginButton().click()
     
    #判断登录是否成功
    def judgeLoginOrNot(self,accountName):
        try:
            WebDriverWait(self.driver,60).until(EC.visibility_of_element_located((By.NAME,accountName)))
            print '%s——>登录成功!' %(accountName)
        except:
            print '%s——>登录失败！' %(accountName)
                
  
    #封装登录方法
    def userLogin(self,username,password):
        self.click_headLogo()
        self.input_userName(username)
        self.input_passWord(password)
        self.click_loginButton()
    
    
#------------------------------------------------------------------------------------------------------------------------------------------------   
    
      
    #定位退出按钮
    def logoutButton(self):
        return self.by_xpath("//android.widget.Button[contains(@text,'安全退出')]")
       
    #点击登录按钮
    def click_logoutButton(self):
        self.logoutButton().click()
        
    #封装退出方法
    def userlogout(self):
        self.click_headLogo()
        self.click_logoutButton()        
        
#-----------------------------------------------------------------------------------------------------------------------------------------------


    #定位“免费注册”
    def freeRegister(self):
        return self.by_name("免费注册")    
    



