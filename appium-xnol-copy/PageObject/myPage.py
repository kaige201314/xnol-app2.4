#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import unittest
import time
from time import sleep
from appium import webdriver
#引入同目录下的BasePage
import BasePage
from BasePage import BaseAction
#引入同目录下的loginPage
import loginPage
from loginPage import LoginPage
#引入智能等待所需要的包
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#引用别的目录中的模块
sys.path.append("..")
#引入手机号自动生成模块
from Public import telePhoneNum
from Public.telePhoneNum import TelePhoneNum
#引入通用方法模块
from Public import common
from Public.common import Common
#引入身份证自动生成模块
from Public import idNo
from Public.idNo import IdNo
#引入银行卡自动生成模块
from Public import cardNo
from Public.cardNo import CardNO
#引入激活码
from Public import read_from_activatronCode
from Public.read_from_activatronCode import Read_from_activatronCode
#引入输入法切换模块
from Public import inputMethod
from Public.inputMethod import InputMethod
#引用数据库模块，在Public目录的db文件中
from Public.db import Db
#引入PageObject目录的loginPage
from PageObject import loginPage
from PageObject.loginPage import LoginPage
#引入存入函数
from Public import write_to_txt
from Public.write_to_txt import Write_to
#引入读取函数
from Public import read_from_txt
from Public.read_from_txt import Read_from
#引入处理excel文件的模块
import xlrd


#设置全局变量
Verification_code='123456'
RealName=u'测试君'
bankName='招商银行'




class MyPage(BasePage.BaseAction):

#手势密码------------------------------------------------------------------------------------------------------------------------------------------------    

    #定位“手势密码页面”的文字
    def gesture_password_page(self):
        #return self.by_id("com.xiaoniu.finance:id/gksGestureResultTv")
        return self.by_xpath("//android.widget.TextView[contains(@text,'请绘制手势密码')]")
    
    #定位“手势密码页面”的跳过按钮
    def gesture_password(self):
        return self.by_id("com.xiaoniu.finance:id/glSkipSet")
    
    #点击“手势密码页面”的跳过按钮
    def click_gesture_password(self):
        self.gesture_password().click()
       
    #判断是否有手势密码页面
    def judge_gesture_password_page(self):
        gesture_password_page_text=self.gesture_password_page().text        
        if gesture_password_page_text == '请绘制手势密码':
            self.click_gesture_password()
        else:
            pass

               
#充值入口、绑卡页面元素的定位和操作------------------------------------------------------------------------------------------------------------------------------------------------   

    #定位“充值金额”输入框
    def rechargeValue_input_Area(self):
        return self.by_id("com.xiaoniu.finance:id/et_input")
    
    #输入“充值金额”，1000元
    def input_rechargeValue(self):
        self.rechargeValue_input_Area().send_keys('1000')
        
    
    #定位“银行卡充值方式”单选框
    def item_bank_check(self):
        return self.by_id("com.xiaoniu.finance:id/item_bank_check")
    
    #选择“银行卡充值方式”
    def choose_item_bank_check(self):
        self.item_bank_check().click()
        
    #定位“充值”按钮
    def recharge_Button(self):
        return self.by_id("com.xiaoniu.finance:id/nextstep_btn")
    
    #点击“充值”按钮
    def click_recharge_Button(self):
        self.recharge_Button().click()
        
    #定位“我的”页面的“充值”按钮
    def myPage_recharge_Button(self):
        return self.by_name("充值")

    
    #点击“我的”页面的“充值”按钮
    def click_myPage_recharge_Button(self):
        self.myPage_recharge_Button().click()
        
        

#开通支付页面的元素定位和操作--------------------------------------------------------------------------------------------------------------------------------
 
    #定位“开通支付页面”的四个输入框 之“真实姓名”输入框
    def realName_input_Area(self):
        return self.by_name("请输入您的开户姓名")
    
    #输入“真实姓名” 
    def input_realName(self):
        global RealName
        self.realName_input_Area().send_keys(RealName)
                
    #定位“开通支付页面”的四个输入框 之“身份证号”输入框
    def idCardNo_input_Area(self):
        return self.by_name("请输入您的身份证号")
    
    #输入“身份证号”
    def intput_idCardNo(self):
        idCardNo=idNo.IdNo().makeNO()
        #将身份证保存进idCardNO.txt
        write_to_txt.Write_to().write_to(idCardNo,'idCardNO.txt')
        self.idCardNo_input_Area().send_keys(idCardNo) 
            
    #定位“开通支付页面”的四个输入框 之“银行卡号”输入框
    def bankCardNo_input_Area(self):
        return self.by_name("请输入您的银行卡号")    
   
    #输入“银行卡号”
    def input_bankCardNo(self):
        global bankName
        bankCardNo=cardNo.CardNO().makeNO(bankName)
        print bankCardNo+"------这是自动生成银行卡号" 
        self.bankCardNo_input_Area().send_keys(bankCardNo)
    
    #由于输入银行卡号之后，会自动匹配银行，所以不需要再做选择银行操作，直接到下一步，输入手机号即可

    #定位“开通支付页面”的四个输入框 之“手机号”输入框
    def preMobileNo_input_Area(self):
        return self.by_name("请输入银行预留手机号")          
    
    #输入银行预留手机号
    def input_preMobileNo(self,preMobileNo):
        self.preMobileNo_input_Area().send_keys(preMobileNo)
         

#验证码页面的元素定位和操作--------------------------------------------------------------------------------------------------------------------------------
        
    #定位验证码输入框
    def verification_code_Area(self):
        return self.by_ids("com.xiaoniu.finance:id/et_input")[0]
        
    #输入验证码
    def input_verification_code(self):
        global Verification_code
        self.verification_code_Area().clear()
        self.verification_code_Area().send_keys(Verification_code)

       
    #定位“完成开通认证”按钮
    def finish_binding_Button(self):
        return self.by_name("完成开通认证")
        
    #点击“完成开通认证”按钮
    def click_finish_binding_Button(self):
        self.finish_binding_Button().click()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,u'充值')))
        
    #点击充值，并输入验证码
    def click_rechargeButton_and_input_verification_code(self):
        global Verification_code
        self.click_recharge_Button()
        self.verification_code_Area().send_keys(Verification_code)
        
    
    #定位“确认充值”按钮
    def confirm_recharge_Button(self):
        return self.by_name("确认充值")
  
       
    #点击“确认充值”按钮
    def cilck_confirm_recharge_Button(self):
        self.confirm_recharge_Button().click()

        
        
#封装绑卡+充值的整个流程--------------------------------------------------------------------------------------------------------------------------------
      
    #封装绑卡+充值方法
    def user_Recharge(self,preMobileNo):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,u'充值'))) 
        self.click_myPage_recharge_Button()
        self.input_rechargeValue()
        self.choose_item_bank_check()
        self.click_recharge_Button()
        sleep(2)
        self.input_realName()
        self.intput_idCardNo()
 
        #切换输入法为latin输入法
        inputMethod.InputMethod().enableLatinIME()
        #输入银行卡号码
        self.input_bankCardNo()
        self.input_preMobileNo(preMobileNo)
        #设置appium输入法为当前输入法
        inputMethod.InputMethod().enableAppiumUnicodeIME()
        #点击"下一步"按钮，由于“下一步”的定为和点击，已经在loginPage中实现了，故直接调用即可
        loginPage.LoginPage(self.driver).click_next_step_Button()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,u'开通认证支付')))   
        self.input_verification_code()
        self.click_finish_binding_Button()
        #点击充值，输入验证码
        self.click_rechargeButton_and_input_verification_code()
        #点击“确认充值”按钮
        self.cilck_confirm_recharge_Button()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,u'恭喜您，充值成功！')))
        #点击返回按钮<,返回到我的页面
        loginPage.LoginPage(self.driver).click_back_Button()
        
        
#提现入口、设置交易密码等页面元素的定位和操作------------------------------------------------------------------------------------------------------------------------------------------------   
    
    #定位提现按钮
    def mypage_cash_withdrawal_Button(self):
        return self.by_name("提现")
    
    #点击提现按钮
    def click_mypage_cash_withdrawal_Button(self):
        self.mypage_cash_withdrawal_Button().click()
        
    #定位还未绑卡时弹出的:绑卡提示框------看情况使用
    def certification_open_Button(self):
        return self.by_xpath("//android.widget.Button[contains(@text,'立即开通')]")
    
    #点击“立即开通”按钮------看情况使用
    def click_certification_open_Button(self):
        self.click_certification_open_Button().clcik()
    
    #定位“提现金额”输入框
    def cash_withdrawal_input_Area(self):
        return self.by_id("com.xiaoniu.finance:id/et_input")
    
    #输入“提现金额”——100元
    def input_cash_withdrawal_Amount(self):
        self.cash_withdrawal_input_Area().send_keys('100')
        
  
    #点击下一步按钮,直接使用LogoinPage中的方法：login.Longin().click_next_step_Button()
    
    #请输入验证码，直接使用loginPage中的方法：login.Longin().input_verification_code(teleNum)


    #定位交易密码输入框
    def trade_code_input_Area(self):
        return self.by_ids("com.xiaoniu.finance:id/et_input")[1]
    
    #输入交易密码
    def input_trade_code(self):
        #读取原交易密码
        tradeCode=read_from_txt.Read_from().read_from('tradeCode.txt')
        self.trade_code_input_Area().send_keys(tradeCode)
        
    #定位“确认提现”按钮
    def confirm_cash_withdrawal_Button(self):
        #return self.by_xpath("//android.widget.Button[contains(@text,'确认提现')]")
        return self.by_id("com.xiaoniu.finance:id/withdraw_btn")
    
    #点击“确认提现”按钮
    def click_confirm_cash_withdrawal_Button(self):
        self.confirm_cash_withdrawal_Button().click()
        
    #定位提现成功页面的元素
    def cash_withdrawal_success_Page(self):
        return self.by_id("com.xiaoniu.finance:id/tv_message")
        
    #点击back按钮，直接使用loginPage里的方法：loginPage.LoginPage().click_back_Button()
    
    #退出登录，也直接用loginPage里的方法：loginPage.LoginPage().userlogout()  
    
#封装提现的整个流程--------------------------------------------------------------------------------------------------------------------------------
    
    #封装提现方法
    def user_cash_Withdrawal(self,teleNum):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,u'提现'))) 
        #点击提现按钮
        self.click_mypage_cash_withdrawal_Button()
        #输入提现金额
        self.input_cash_withdrawal_Amount()
        #点击下一步按钮
        loginPage.LoginPage(self.driver).click_next_step_Button()
        sleep(2)
        #输入验证码
        loginPage.LoginPage(self.driver).input_verification_code(teleNum)
        #输入交易密码
        self.input_trade_code()
        #点击确认提现按钮
        self.click_confirm_cash_withdrawal_Button()
        sleep(2)
        #等待提现成功页面出现
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'提现到账时间说明')))  
        #点击返回键 
        loginPage.LoginPage(self.driver).click_back_Button()
        
        
#封装添加理财金券的整个流程--------------------------------------------------------------------------------------------------------------------------------

    #定位“红包优惠券”入口
    def redbag_and_coupons(self):
        return self.by_name("红包优惠券")
       
    #点击“红包优惠券”
    def click_redbag_and_coupons(self):
        self.redbag_and_coupons().click()

    #定位“理财金券”入口
    def financial_coupons(self):
        return self.by_name("理财金券")
       
    #点击“理财金券”
    def click_financial_coupons(self):
        self.financial_coupons().click()
        
    #定位“添加理财金券”入口
    def add_financial_coupons_in(self):
        return self.by_name("添加理财金券")
       
    #点击“添加理财金券”
    def click_add_financial_coupons(self):
        self.add_financial_coupons_in().click()
        
    #定位“激活码”输入框
    def activation_code_input_Area(self):
        return self.by_name("请输入激活码")
          
    #输入“激活码”
    def input_activation_code(self,activatronCode):
        self.activation_code_input_Area().send_keys(activatronCode)
        
    #点击“确定”按钮，直接使用： loginPage.LoginPage().click_confirm_Button() 
        
        

    #封装添加理财金券的方法
    def add_financial_coupons_function(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'充值')))
        #向上滑动
        self.swipe('up',100)
        self.click_redbag_and_coupons()
        self.click_financial_coupons()
        self.click_add_financial_coupons()
        #读取激活码
        activatronCode=read_from_activatronCode.Read_from_activatronCode().read_activatronCode()        
        #输入激活码
        self.input_activation_code(activatronCode)
        #点击确定按钮
        loginPage.LoginPage(self.driver).click_confirm_Button()
        #点击返回键 
        loginPage.LoginPage(self.driver).click_back_Button()
        self.swipe('down',100)
        
        
        
        
        
        
        
        
#封装提取天天牛、月月牛的整个流程--------------------------------------------------------------------------------------------------------------------------------

    #定位“我的天天牛”入口
    def my_current_interest(self):
        return self.by_name("我的天天牛")
    
    #点击“我的天天牛”入口
    def click_my_current_interest(self):
        self.my_current_interest().click()
        
    #定位“我的月月牛”入口
    def my_smart_interest(self):
        return self.by_name("我的月月牛")
    
    #点击“我的月月牛”入口
    def click_my_smart_interest(self):
        self.my_smart_interest().click() 
        
    #定位“提取”按钮,定位我的月月牛页面的所有提取按钮的第一个
    def extract_Button1(self):
        return self.by_names("提取")[0]

    #点击"提取"按钮
    def click_extract_Button1(self):
        self.extract_Button1().click()
        
    #定位"提取金额"输入框
    def extract_amount_input_Area(self):
        return self.by_ids("com.xiaoniu.finance:id/et_input")[0]
    
    #点击并输入"提取金额"100元
    def input_extract_amount(self,amount):
        self.extract_amount_input_Area().send_keys(amount)    

    
    #定位"交易密码"输入框
    def tradeCode_input_Area(self):
        return self.by_ids("com.xiaoniu.finance:id/et_input")[1]
    
    #点击并输入"交易密码"
    def input_tradeCode(self,tradeCode):
        self.trade_code_input_Area().send_keys(tradeCode)

    #定位“提取”按钮
    def extract_Button2(self):
        return self.by_name("提取")

    #点击"提取"按钮
    def click_extract_Button2(self):
        self.extract_Button2().click()
        
    #定位“确定提取”按钮
    def confirm_extract_Button(self):
        return self.by_name("确定提取")


    #点击"提取"按钮
    def click_confirm_extract_Button(self):
        self.confirm_extract_Button().click()
        
    #点击提取按钮，直接使用：click_extract_Button()
    #点击“确定”按钮，直接使用： loginPage.LoginPage().click_confirm_Button() 
    #WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'恭喜您，提取申请已提交成功')))
    
    #封装提取月月牛的方法
    def smart_interest_extract(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'充值')))        
        self.click_my_smart_interest()
        sleep(3)
        #向上滑动
        self.swipe('up',2000)
        self.swipe('up',2000)
        self.click_extract_Button1()
        self.input_extract_amount('100')
        self.input_tradeCode('123456')
        self.click_extract_Button2()
        loginPage.LoginPage(self.driver).click_confirm_Button()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'恭喜您，提取申请已提交成功')))
        #点击返回按钮<，点2次，返回到我的页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        
   
    #封装提取天天牛的方法
    def current_interest_extract(self): 
        self.click_my_current_interest()
        self.click_extract_Button2()
        self.input_extract_amount('1')
        self.input_tradeCode('123456')
        self.click_confirm_extract_Button()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'恭喜您，提取申请已提交成功')))
        #点击返回按钮<，点2次，返回到我的页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()

        
        
        
        
        
        
        
        
        
        
        
        