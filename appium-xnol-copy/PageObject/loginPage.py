#coding=utf-8
import sys
from macpath import split
reload(sys)
sys.setdefaultencoding('utf8')

import os
import unittest
import time
from time import sleep
#引用同目录下，别的模块
import BasePage
from BasePage import BaseAction
from appium import webdriver
#智能等待引包
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#引用别的目录中的模块
sys.path.append("..")
#引入手机号自动生成模块
from Public import telePhoneNum
from Public.telePhoneNum import TelePhoneNum
#引入通用模块
from Public import common
from Public.common import Common
#引入输入法切换模块
from Public import inputMethod
from Public.inputMethod import InputMethod
#引入存入函数
from Public import write_to_txt
from Public.write_to_txt import Write_to
#引入读取函数
from Public import read_from_txt
from Public.read_from_txt import Read_from
#引用数据库模块，在Public目录的db文件中
from Public.db import Db


#将手机号设置为全局变量，初始值为0
mobelNo='0'          
#用户注册的初始密码，初始值为a12345678，静态全局变量
orginal_password='a12345678'

   
    
class LoginPage(BasePage.BaseAction):
    
#公用------------------------------------------------------------------------------------------------------------------------------------------------

    #定位我的页面
    def getMyPage(self):
        return self.by_name('我的')
    
    #定位用户头像（无论是否登录，头像的id不会变）
    def getAccount_header(self):
        return self.by_id("com.xiaoniu.finance:id/account_header")
        
    #点击用户头像，进入登录页面（未登录）/用户信息页面（已登录）
    def click_headLogo(self):
        #首先返回到"我的"页面
        #Dash(driver).recover()
        sleep(3)
        self.getMyPage().click()
        self.getAccount_header().click()
        sleep(2)

#登录过程------------------------------------------------------------------------------------------------------------------------------------------------
    
    #定位用户名输入框
    def username(self):
        return self.by_ids("com.xiaoniu.finance:id/et_input")[0]
        
    #定位密码输入框
    def password(self):
        return self.by_ids("com.xiaoniu.finance:id/et_input")[1]
    
    #定位登录框，先清理一下，再输入用户名
    def input_userName(self,username):
        self.username().clear()
        self.username().send_keys(username)
        
    #定位登录框，输入密码
    def input_passWord(self,password):
        self.password().send_keys(password)
    
    #定位登录按钮
    def loginButton(self):
        return self.by_xpath("//android.widget.Button[contains(@text,'登录')]")
       
    #点击登录按钮
    def click_loginButton(self):
        self.loginButton().click()
     
#判断登录是否成功，后面看情况考虑是否加断言
#     def judgeLoginOrNot(self,accountName):
#         try:
#             WebDriverWait(self.driver,60).until(EC.visibility_of_element_located((By.NAME,accountName)))
#             print '%s——>登录成功!' %(accountName)
#         except:
#             print '%s——>登录失败！' %(accountName)
                
  
    #封装登录方法
    def userLogin(self,username,password):

        self.click_headLogo()
        self.input_userName(username)
        self.input_passWord(password)
        self.click_loginButton()
    
    
#退出过程------------------------------------------------------------------------------------------------------------------------------------------------   
    
      
    #定位“安全退出”按钮
    def logoutButton(self):
        return self.by_xpath("//android.widget.Button[contains(@text,'安全退出')]")
       
    #点击“安全退出”按钮
    def click_logoutButton(self):
        self.logoutButton().click()
        
    #封装退出方法
    def userlogout(self):
        self.click_headLogo()
        self.click_logoutButton() 
        
        
               
        
#注册过程-----------------------------------------------------------------------------------------------------------------------------------------------


    #定位“免费注册领红包”按钮
    def freeRegister(self):
        return self.by_id("com.xiaoniu.finance:id/ll_register")
    
    #点击“免费注册领红包”按钮
    def click_registerButton(self):
        self.freeRegister().click()

        
    #定位手机号输入框
    def mobileNo_input_Area(self):
        return self.by_ids("com.xiaoniu.finance:id/et_input")[0]     
        
    #输入手机号
    def input_mobileNo(self):
        global mobileNo
        mobileNo=telePhoneNum.TelePhoneNum().phoneNum()
        self.mobileNo_input_Area().clear()       
        self.mobileNo_input_Area().send_keys(mobileNo)
           

    #定位下一步按钮
    def next_step_Button(self):
        return self.by_xpath("//android.widget.Button[contains(@text,'下一步')]")
    
    #点击下一步按钮
    def click_next_step_Button(self):
        self.next_step_Button().click()

    
    #定位“确定”按钮
    def confirm_Button(self):  
        return self.by_xpath("//android.widget.Button[contains(@text,'确定')]")
    
    #点击“确定”按钮
    def click_confirm_Button(self):
        self.confirm_Button().click()
        #WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.ID,'com.xiaoniu.finance:id/titlebar_tv_center')))
        #WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,u'设置密码')))
 
    

    
    
    #定位设置登录密码框
    def password_set_Area(self):
        return self.by_ids("com.xiaoniu.finance:id/et_input")[0]
    
    #输入想设置的登录密码
    def set_password(self):
        global orginal_password
        self.password_set_Area().click()
        #将原始登录密码保存进login_password.txt
        write_to_txt.Write_to().write_to(orginal_password,'login_password.txt')
        self.password_set_Area().send_keys(orginal_password)
    
    
    #定位验证码输入框
    def verification_code_Area(self):
        return self.by_name("请输入验证码")

    
    #定位“获取验证码”按钮
    def get_verification_code_Button(self):
        return self.by_id("com.xiaoniu.finance:id/btn_countdown")

    
    #点击“获取验证码”按钮
    def click_get_verification_code_Button(self):
        self.get_verification_code_Button().click()
        
    
   
    #获取验证码的方法
    def get_verification_code(self,teleNum):
        #在xnmsg数据库中查询对应手机号mobileNo的短信内容，"+teleNum+"这些写是为了传递变量值teleNum进去
        content=Db("xnmsg").sql("SELECT content FROM sms_sendlog_his WHERE mobile="+teleNum+" ORDER BY id DESC LIMIT 1 ")
        sleep(5)
        content=str(content)
        #将短信中的验证码过滤出来，抽取字符串中的数字用filter(str.isdigit, item)
        verification_code=filter(str.isdigit,content.encode('UTF-8'))
        print verification_code+'-------验证码'
        return verification_code         
        
    #输入验证码
    def input_verification_code(self,mobileNo):
        print mobileNo+"-------查询该手机号的验证码"
        verification_code=self.get_verification_code(mobileNo)
        self.verification_code_Area().clear()
        self.verification_code_Area().send_keys(verification_code)
        
        
    #定位“完成注册”按钮    
    def finish_Register_Button(self):
        return self.by_id("com.xiaoniu.finance:id/register")
        #return self.by_xpath("//android.widget.Button[contains(@text,u'完成注册')]")

    #点击“完成注册”按钮
    def click_finish_Register_Button(self):
        self.finish_Register_Button().click()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'注册成功')))
                
   
    
    #定位“充值领红包”按钮
    def get_redbag_and_recharge_Button(self):
        return self.by_id("com.xiaoniu.finance:id/btn_get")
        #return self.by_xpath("//android.widget.Button[contains(@text,'充值领红包')]")
        
    #点击“充值领红包”按钮
    def click_get_redbag_and_recharge_Button(self):
        self.get_redbag_and_recharge_Button().click()


    #定位“<”回退按钮
    def back_Button(self):
        return self.by_id("com.xiaoniu.finance:id/titlebar_tv_left")
        #return self.by_xpath("//android.widget.TextView[contains(@text,'<')]")
        
    #点击“<”回退按钮
    def click_back_Button(self):
        self.back_Button().click()

    #将自动生成的手机号写入PhoneNO.txt文件
    def write_to_PhoneNO(self,PhoneNO):
        p='Data/phoneNO.txt'
        #获取当前文件的绝对路径，然后拼接p
        phoneNO_txt_url=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, p))
        f=open(phoneNO_txt_url,'w')
        f.write(PhoneNO)
        f.flush()
        f.close()
        print PhoneNO+"————mobileNo，已经写入PhoneNO.txt文件中了" 


 
    #封装注册方法：
    def user_Register(self):
        self.click_headLogo()
        self.click_registerButton()
        #切换输入法为latin输入法
        inputMethod.InputMethod().enableLatinIME()
        #输入手机号
        self.input_mobileNo()        
        #设置appium输入法为当前输入法
        inputMethod.InputMethod().enableAppiumUnicodeIME()
        self.click_next_step_Button()
        self.click_confirm_Button()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,u'设置密码')))
        self.set_password()
        self.click_get_verification_code_Button()
        global mobileNo
        self.input_verification_code(mobileNo)
        self.click_finish_Register_Button()
        #将自动生成的手机号写入PhoneNO.txt文件
        self.write_to_PhoneNO(mobileNo)
        sleep(3)
        self.click_back_Button()


        
        
        
        
        
        
    
    



