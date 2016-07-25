#coding=utf-8
import sys
from lib2to3.pgen2.driver import Driver
reload(sys)
sys.setdefaultencoding('utf8')

import unittest
import time
from time import sleep
from appium import webdriver
#引入同目录下的BasePage
import BasePage
from BasePage import BaseAction
#引入同目录下的loginPage
from PageObject import loginPage
from PageObject.loginPage import LoginPage
#引入TouchAction所需要的包
from appium.webdriver.common.touch_action import TouchAction
#引入智能等待所需要的包
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#引用别的目录中的模块
sys.path.append("..")
#引入手机号自动生成模块
from Public import gVariable
from Public.gVariable import GVariable
#引入通用方法模块
from Public import common
from Public.common import Common
#引入身份证自动生成模块
from Public import idNo
from Public.idNo import IdNo
#引入银行卡自动生成模块
from Public import cardNo
from Public.cardNo import CardNO
#引入存入函数
from Public import write_to_txt
from Public.write_to_txt import Write_to
#引入读取函数
from Public import read_from_txt
from Public.read_from_txt import Read_from
#引用数据库模块，在Public目录的db文件中
from Public.db import Db




#交易密码
tradeCode='a123456789'
findback_tradeCode='a123456789'


class AccountPage(BasePage.BaseAction):

#公用方法--------------------------------------------------------------------------------------------------------------------------------------------------------
    
    #登录之后点击用户头像:loginPage.LoginPage().click_headLogo()
    
    #定位“密码安全”区域
    def code_security_Area(self):
        return self.by_name("密码安全")
    
    #点击“密码安全”区域
    def click_code_security_Area(self):
        self.code_security_Area().click()
        
#封装修改登录密码的整个流程--------------------------------------------------------------------------------------------------------------------------------

    #定位登录密码的“修改”
    def loginPassword_change_Area(self):
        return self.by_names("修改")[0]
    
    #点击“修改”
    def click_loginPassword_change_Area(self):
        self.loginPassword_change_Area().click()
        
    #定位“请输入原密码"框
    def old_password_input_Area(self):
        return self.by_name("请输入原密码")
        
    #输入原密码
    def input_old_password(self,oldPassword):
        self.old_password_input_Area().send_keys(oldPassword)
        
    #定位新登录密码输入框
    def new_password_input_Area(self):
        return self.by_name("8-20位，数字、字母或符号组合")
    
    #输入新登录密码，第一次输入
    def input_new_password(self,newPassword):
        self.new_password_input_Area().send_keys(newPassword)
    
    #定位确认新登录密码输入框   
    def confirm_new_password_input_Area(self):
        return self.by_name("重新输入新密码")
    
    #确认输入新密码交易，第二次输入
    def confirm_input_new_password(self,newPassword):
        self.confirm_new_password_input_Area().send_keys(newPassword)
        
    #定位完成按钮    
    def finish_Button(self):
        return self.by_name("完成")
    
    #点击完成按钮
    def click_finish_Button(self):
        self.finish_Button().click()
        
    #定位“知道了”
    def iknow_Button(self):
        return self.by_name("知道了")
    
    #点击“知道了”
    def click_iknow_Button(self):
        self.iknow_Button().click()
       

    #封装修改登录密码的方法
    def change_loginPassword(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'充值')))
        #点击用户头像
        loginPage.LoginPage(self.driver).click_headLogo()
        #点击密码安全区域
        self.click_code_security_Area()
        #点击登录密码右侧的“修改”
        self.click_loginPassword_change_Area()
        #读取登录密码
        oldPassword=read_from_txt.Read_from().read_from('login_password.txt')
        newPassword=oldPassword+'1'
        #输入原密码
        self.input_old_password(oldPassword)
        #输入新密码，第一次
        self.input_new_password(newPassword)   
        #确认输入新密码，第二次
        self.confirm_input_new_password(newPassword)
        #将新登录密码保存进login_password.txt
        write_to_txt.Write_to().write_to(newPassword,'login_password.txt')
        #点击“完成”按钮
        self.click_finish_Button()        
        #点击“知道了”
        self.click_iknow_Button()   
        






#封装设置交易密码的整个流程--------------------------------------------------------------------------------------------------------------------------------

    #定位“交易密码”区域
    def trade_code_Area(self):
        return self.by_name("交易密码")
    
    #点击“交易密码”区域
    def click_trade_code_Area(self):
        self.trade_code_Area().click()    
        
    #输入验证码：loginPage.LoginPage().input_verification_code(teleNum)
    
    #点击下一步：loginPage.LoginPage().click_next_step_Button()
    
    #定位“设置交易密码”框
    def trade_code_set_Area(self):
        return self.by_name("请输入交易密码")
    
    #输入“交易密码”
    def set_trade_code(self,code):
        self.trade_code_set_Area().send_keys(code)
    
    #定位“确认交易密码”框
    def confirm_trade_code_set_Area(self):
        return self.by_name("请再次输入交易密码")    
    
    #再次输入交易密码
    def confirm_trade_code(self,code):
        self.confirm_trade_code_set_Area().send_keys(code)
        
    
    #点击“确定”按钮：loginPage.LoginPage().click_confirm_Button()
    
    #设置交易密码成功:WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'恭喜您，交易密码设置成功！')))
    
    #点击返回按钮：loginPage.LoginPage().click_back_Button()
    
    #封装设置交易密码的方法
    def set_tradeCode(self,teleNum):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'充值')))
        #点击用户头像
        loginPage.LoginPage(self.driver).click_headLogo()
        #点击密码安全区域
        self.click_code_security_Area()
        #点击交易密码区域
        self.click_trade_code_Area()
        #输入验证码
        loginPage.LoginPage(self.driver).input_verification_code(teleNum)
        #点击下一步按钮
        loginPage.LoginPage(self.driver).click_next_step_Button()
        #设置交易密码
        global tradeCode
        self.set_trade_code(tradeCode)
        #确认交易密码
        self.confirm_trade_code(tradeCode)
        
        #将新交易密码保存进tradeCode.txt
        write_to_txt.Write_to().write_to(tradeCode,'tradeCode.txt')
        
        #点击确定按钮
        loginPage.LoginPage(self.driver).click_confirm_Button()
        #等待设置交易密码成功页面出现
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'恭喜您，交易密码设置成功！')))
        #点击返回按钮<，点三次，返回到我的页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()


        
#封装修改交易密码的整个流程--------------------------------------------------------------------------------------------------------------------------------
    
    #定位旧交易密码输入框 
    def old_tradecode_input_Area(self):
        return self.by_name("请输入原密码")
    
    #输入旧交易密码   
    def input_old_tradecode(self,tradeCode):
        self.old_tradecode_input_Area().send_keys(tradeCode)
        
    #请输入验证码：loginPage.LoginPage().input_verification_code(teleNum)
     
    #定位新交易密码输入框   
    def new_tradeCode_set_Area(self):
        return self.by_name("8-20位，数字、字母或符号组合")
    
    #输入新交易密码，第一次输入
    def set_new_tradeCode(self,code):
        self.new_tradeCode_set_Area().send_keys(code)
    
    #定位新交易密码输入框   
    def confirm_new_tradeCode_set_Area(self):
        return self.by_name("重新输入新密码")
    
    #确认输入新密码交易，第二次输入
    def confirm_set_new_tradeCode(self,code):
        self.confirm_new_tradeCode_set_Area().send_keys(code)
    
       
    #封装修改交易密码的方法
    def change_tradeCode(self,teleNum):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'充值')))
        #点击用户头像
        loginPage.LoginPage(self.driver).click_headLogo()
        #点击密码安全区域
        self.click_code_security_Area()
        #点击交易密码区域
        self.click_trade_code_Area()
        #读取原交易密码
        tradeCode=read_from_txt.Read_from().read_from('tradeCode.txt')
        #输入原交易密码        
        self.input_old_tradecode(tradeCode)
        #输入验证码
        loginPage.LoginPage(self.driver).input_verification_code(teleNum)
        #输入新交易密码
        new_tradeCode=tradeCode+'1'
        self.set_new_tradeCode(new_tradeCode)
        #确认输入新交易密码
        self.confirm_set_new_tradeCode(new_tradeCode)
        
        #将新交易密码保存进tradeCode.txt
        write_to_txt.Write_to().write_to(new_tradeCode,'tradeCode.txt')   
          
        #点击完成按钮
        self.finish_Button().click()
        #点击返回按钮<，连续2次，返回到我的页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()

        
#封装找回交易密码的整个流程--------------------------------------------------------------------------------------------------------------------------------
    #定位“忘记交易密码”
    def forget_tradeCode(self):
        return self.by_name("忘记交易密码？")
    
    #点击“忘记交易密码”
    def click_forget_tradeCode(self):
        self.forget_tradeCode().click()
        
#     #定位"身份证号"输入框
#     def idCardNO_input_Area(self):
#         return self.by_name("请输入您的身份证号")
#     
#     
#     def get_idCardNO(self,teleNum):
#         #在xnmsg数据库中查询对应手机号mobileNo的身份证号，"+teleNum+"这些写是为了传递变量值teleNum进去
#         content=Db("xnmsg").sql("SELECT content FROM sms_sendlog_his WHERE mobile="+teleNum+" ORDER BY id DESC LIMIT 1 ")
#         sleep(5)
#         content=str(content)
#         #将短信中的验证码过滤出来，抽取字符串中的数字用filter(str.isdigit, item)
#         idCardNO=filter(str.isdigit,content.encode('UTF-8'))
#         print idCardNO+'-------身份证号'
#         return idCardNO
#         
#     
#     #输入“身份证号”
#     def input_idCardNO(self):
#         self
        
        
    
    
    
    #封装找回交易密码的方法，由于身份证号码是加密处理的，从数据库查出来都是密文，所以此条用例必须在绑卡之前执行
    def findback_tradeCode(self,teleNum):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'充值')))
        #点击用户头像
        loginPage.LoginPage(self.driver).click_headLogo()
        #点击密码安全区域
        self.click_code_security_Area()
        #点击交易密码区域
        self.click_trade_code_Area()
        #点击“忘记交易密码”
        self.click_forget_tradeCode()
        #输入验证码
        loginPage.LoginPage(self.driver).input_verification_code(teleNum)        
        #点击下一步按钮
        loginPage.LoginPage(self.driver).click_next_step_Button()
        #输入新密码第一次
        global findback_tradeCode
        self.set_new_tradeCode(findback_tradeCode)
        #输入新密码第二次
        self.confirm_set_new_tradeCode(findback_tradeCode)
        
        #将“找回易密码findback_tradeCode”保存进tradeCode.txt
        write_to_txt.Write_to().write_to(findback_tradeCode,'tradeCode.txt')      
        
        #点击确定按钮
        loginPage.LoginPage(self.driver).click_confirm_Button()
        #点击返回<,连续2次，返回到我的页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        
        
        
        
        
        
    
    
#封装设置手势密码的整个流程--------------------------------------------------------------------------------------------------------------------------------

            
    #定位“手势密码”开关
    def registrue_code_Area(self):
        return self.by_id("com.xiaoniu.finance:id/cbitCheckBox")
    
    #点击“手势密码”开关
    def click_registrue_code_Area(self):
        self.registrue_code_Area().click()
        
    #定位手势密码的“修改”开关
    def registrue_code_change(self):
        return self.by_names("修改")[1]
    
    #点击修改手势密码开关
    def change_registrue_code(self):
        self.registrue_code_change().click()
    
    #定位手势密码的所有位置元素
    def elements(self):
        return self.by_class_names("android.view.View")
    
    #绘制手势密码"L"
    def set_Gesture1(self):
        el=self.elements()
        #TouchAction(self.driver).press(el[3]).move_to(el[4]).wait(100).move_to(el[5]).wait(100).move_to(el[6]).wait(100).move_to(el[7]).release().perform()
        #TouchAction(self.driver).press(el[3]).move_to(el[7]).wait(100).move_to(el[6]).wait(100).move_to(el[5]).wait(100).move_to(el[4]).release().perform()
        #TouchAction(self.driver).press(el[2]).move_to(el[5]).wait(100).move_to(el[6]).wait(100).move_to(el[8]).wait(100).move_to(el[9]).release().perform()
        TouchAction(self.driver).press(el[3]).move_to(el[3]).wait(100).move_to(el[6]).wait(100).move_to(el[9]).wait(100).move_to(el[10]).release().perform()

    #绘制手势密码""
    def set_Gesture2(self):
        el=self.elements()
        TouchAction(self.driver).press(el[2]).move_to(el[2]).wait(100).move_to(el[5]).wait(100).move_to(el[8]).wait(100).move_to(el[9]).release().perform()
        

    #封装设置手势密码的方法
    def set_userGesture(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'充值')))
        #点击用户头像
        loginPage.LoginPage(self.driver).click_headLogo()
        #点击密码安全区域
        self.click_code_security_Area()
        #打开手势密码开关
        self.click_registrue_code_Area()
        #绘制手势密码,连续绘制2次以确定手势密码
        print "绘制手势密码第1次-----------"
        self.set_Gesture1()
        print "绘制手势密码第2次-----------"
        self.set_Gesture1()
        #点击返回按钮<，连续2次，返回到我的页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        
        
    #封装修改手势密码的方法
    def change_userGesture(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'充值')))
        #点击用户头像
        loginPage.LoginPage(self.driver).click_headLogo()
        #点击密码安全区域
        self.click_code_security_Area()
        #点击修改手势密码开关
        self.change_registrue_code()
        #绘制手势密码,连续绘制2次以确定手势密码
        print "绘制手势密码第1次，绘制原手势密码-----------"
        self.set_Gesture2()
        print "绘制手势密码第2次，绘制新手势密码-----------"
        self.set_Gesture1()
        print "绘制手势密码第2次，绘制新手势密码-----------"
        self.set_Gesture1()
        #点击返回按钮<，连续2次，返回到我的页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        
    
       
    #封装正常关闭手势密码的方法
    def close_userGesture(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'充值')))
        #点击用户头像
        loginPage.LoginPage(self.driver).click_headLogo()
        #点击密码安全区域
        self.click_code_security_Area()
        #打开手势密码开关
        self.click_registrue_code_Area()
        #绘制手势密码1次，以关闭手势密码
        self.set_Gesture2()
        #点击返回按钮<，连续2次，返回到我的页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
    
        
    #注册成功之后，立即关闭手势密码
    def close_Rgesture_after_Register(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'充值')))
        #点击用户头像
        loginPage.LoginPage(self.driver).click_headLogo()
        #点击密码安全区域
        self.click_code_security_Area()
        #打开手势密码开关
        self.click_registrue_code_Area()
        #点击返回按钮<，连续3次，返回到我的页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()

       
        
        
        
        
    
