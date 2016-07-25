#coding=utf-8
import sys
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
#引用数据库模块，在Public目录的db文件中
from Public.db import Db


class FinancePage(BasePage.BaseAction):

#公用方法--------------------------------------------------------------------------------------------------------------------------------------------------------
    
    #定位"理财"页面
    def financePage(self):
        return self.by_name('理财')
    
    #点击“理财”
    def clcik_financePage(self):
        self.financePage().click()
        
    #定位“项目分类”
    def projectType(self):
        return self.by_name("项目分类")
   
    #点击“项目分类”
    def click_projectType(self):
        self.projectType().click()
    
    #先定位到理财页，再进入项目分类页面
    def finance_to_projectType(self):
        sleep(3)
        self.clcik_financePage()
        self.click_projectType()
        sleep(2)
        
    
    
    
    
    #定位某个项目列表的第1个标的
    def project_list_choose_first(self):
        return self.by_ids("com.xiaoniu.finance:id/pivh_tv_rate")[0]
    
    #定位某个项目列表的第2个标的
    def project_list_choose_second(self):
        return self.by_ids("com.xiaoniu.finance:id/pivh_tv_rate")[1]
    
    #定位某个项目列表的第3个标的
    def project_list_choose_third(self):
        return self.by_ids("com.xiaoniu.finance:id/pivh_tv_rate")[2]
        
    #点击安心牛项目列表的第1个标的
    def click_project_list_choose_first(self):
        self.project_list_choose_first().click()
        
    #点击安心牛项目列表的第2个标的
    def click_project_list_choose_second(self):
        self.project_list_choose_second().click()

    #点击安心牛项目列表的第3个标的
    def click_project_list_choose_third(self):
        self.project_list_choose_third().click()  
    
    
    
#     #定位加入金额输入框---加入金额
#     def jion_interest_amount_input_Area(self):
#         return self.by_name("请输入加入金额")
#     
#     #输入加入金额---加入金额
#     def input_jion_interest_amount(self):
#         self.jion_interest_amount_input_Area().send_keys('100')
   
#     #定位“立即加入”按钮
#     def join_now_Button(self):
#         return self.by_name("立即加入")
#     
#     #点击“立即加入”按钮
#     def click_join_now_Button(self):
#         self.join_now_Button().click()     
#         
#         

        
#     #定位购买金额输入框---购买金额
#     def interest_amount_input_Area(self):
#         return self.by_name("请输入购买金额")
#     
#     #输入购买金额---购买金额
#     def input_interest_amount(self):
#         self.interest_amount_input_Area().send_keys('100')  


        
        
    #定位“购买金额”/“加入金额”输入框
    def amount_input_Area(self):
        return self.by_id("com.xiaoniu.finance:id/view_input")
    
    #输入“购买金额”/“加入金额”
    def input_amount(self,amount):
        self.amount_input_Area().send_keys(amount)
        
    #定位“立即购买”/"立即加入"按钮
    def buy_Buton(self):
        return self.by_id("com.xiaoniu.finance:id/tv_buy")

    #点击“立即购买”/"立即加入"按钮 
    def click_buy_Buton(self):
        self.buy_Buton().click()   
    
    
    
    
    
    
    #定位“立即购买”按钮
    def buy_now_Buton(self):
        return self.by_name("立即购买")
 
    #点击“立即购买”按钮    
    def click_buy_now_Buton(self):
        self.buy_now_Buton().click()    
       
    #定位“天天牛”+“月月牛”的购买金额输入框,因为天天牛和月月牛的金额输入框id和别的不一样，所以必须重写方法，不能使用公共方法
    def current_smart_amount_input_Area(self):
        return self.by_id("com.xiaoniu.finance:id/et_input")
    
    #输入“天天牛”购买金额
    def input_current_smart_amount(self,amount):
        self.current_smart_amount_input_Area().send_keys(amount)
        
    #定位“确定购买”按钮
    def confirm_buy_Button(self):
        return self.by_id("com.xiaoniu.finance:id/btn_submit")
    
    #点击“确定购买”按钮
    def click_confirm_buy_Button(self):
        self.confirm_buy_Button().click()
    
        


#封装购买“天天牛”的整个过程--------------------------------------------------------------------------------------------------------------------------------------------------------
        
    #定位“天天牛”项目
    def current_interest_project(self):
        return self.by_name("天天牛")
    
    #点击“天天牛”项目
    def click_current_interest_project(self):
        self.current_interest_project().click()    
        
    #封装天天牛的购买方法            
    def buy_current_interest_project(self):
        #点击进入天天牛页面
        self.click_current_interest_project()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'立即购买')))
        #点击“立即购买”按钮，进入“天天牛”购买页面
        self.click_buy_now_Buton()
        self.input_current_smart_amount('100')
        self.click_confirm_buy_Button()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'购买结果')))
        #点击返回按钮<，点2次，返回到项目分类页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()

        
                

#封装购买“月月牛”的整个过程--------------------------------------------------------------------------------------------------------------------------------------------------------
    
    #定位“月月牛”项目
    def smart_interest_project(self):
        return self.by_name("月月牛")
    
    #点击“月月牛”项目
    def click_smart_interest_project(self):
        self.smart_interest_project().click()

    #封装月月牛的购买方法    
    def buy_smart_interest_project(self):
        #点击进入月月牛页面
        self.click_smart_interest_project()
        #点击第一个标，进入“月月牛”购买页面
        self.click_project_list_choose_first()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'立即购买')))
        self.click_buy_now_Buton()
        self.input_current_smart_amount('100')
        self.click_confirm_buy_Button()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'购买结果')))
        #点击返回按钮<，点3次，返回到项目分类页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
   
    

    
#封装购买“安心牛”的整个过程--------------------------------------------------------------------------------------------------------------------------------------------------------

    #定位“安心牛”项目
    def optimiz_interest_project(self):
        return self.by_name("安心牛")
    
    #点击“安心牛”项目
    def click_optimiz_interest_project(self):
        self.optimiz_interest_project().click()  
    
    #封装安心牛的购买方法
    def buy_optimiz_interest_project(self):
        #点击进入安心牛页面
        self.click_optimiz_interest_project()
        sleep(3)
        #点击第一个标，进入安心牛购买页面 
        self.click_project_list_choose_second()
        self.input_amount('100')
        #点击物理机的回退建
        self.driver.keyevent(4)
        self.click_buy_Buton()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'加入结果')))
        #点击返回按钮<，点3次，返回到项目分类页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()

        
        
#封装购买“散标”的整个过程--------------------------------------------------------------------------------------------------------------------------------------------------------

    #定位“散标投资”项目
    def scattered_interest_project(self):
        return self.by_name("散标投资")
    
    #点击“散标投资”项目
    def click_scattered_interest_project(self):
        self.scattered_interest_project().click()
   
    #封装散标的购买方法
    def buy_scattered_interest_project(self):
        #点击进入散标投资页面
        self.click_scattered_interest_project()
        sleep(3)
        #点击第一个标，进入散标购买页面 
        self.click_project_list_choose_first()
        self.input_amount('100')
        #点击物理机的回退建
        self.driver.keyevent(4)
        self.click_buy_Buton()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'购买结果')))
        #点击返回按钮<，点3次，返回到项目分类页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        

#封装购买“富盈人生”的整个过程--------------------------------------------------------------------------------------------------------------------------------------------------------

    #定位“富盈人生”项目
    def fuying_life_interest_project(self):
        return self.by_name("富盈人生")
    
    #点击“富盈人生”项目
    def click_fuying_life_interest_project(self):
        self.fuying_life_interest_project().click()
        
  
    #封装富盈人生的购买方法
    def buy_fuying_life_interest_project(self):
        #点击进入富盈人生页面        
        self.click_fuying_life_interest_project()
        sleep(3)
        #点击第一个标，进入富盈人生购买页面        
        self.click_project_list_choose_first()
        self.input_amount('100')
        #点击物理机的回退建
        self.driver.keyevent(4)
        self.click_buy_Buton()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'购买结果')))
        #点击返回按钮<，点3次，返回到项目分类页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
                

#封装购买“债权转让”的整个过程--------------------------------------------------------------------------------------------------------------------------------------------------------

    #注意：“债权转让”项目需要到web端发起债权转让申请，暂时没有，延后再编写用例

    #定位“债权转让”项目
    def rights_transfer_project(self):
        return self.by_name("债权转让")
    
    #点击“债权转让”项目
    def click_rights_transfer_project(self):
        self.rights_transfer_project().click()
        
    def buy_rights_transfer_project(self):
        self.click_rights_transfer_project()
        
        
        
        
#封装购买“VIP专享”的整个过程--------------------------------------------------------------------------------------------------------------------------------------------------------

    #定位“VIP专享”项目，VIP标仅限银牌以上用户购买，所以必须找到一个等级高的用户单独执行此条用例
    def VIP_exclusive_prpject(self):
        return self.by_name("VIP专享")
    
    #点击“VIP专享”项目
    def clcik_VIP_exclusive_prpject(self):
        self.VIP_exclusive_prpject().click()

    #封装“VIP专享”的购买方法
    def buy_VIP_exclusive_prpject(self):
        self.finance_to_projectType()
        #点击进入VIP项目列表   
        self.clcik_VIP_exclusive_prpject()
        sleep(3)
        #点击第一个标，进入"VIP专享"购买页面    
        self.click_project_list_choose_first()
        #输入购买金额100元
        self.input_amount('100')
        #点击物理机的回退建
        self.driver.keyevent(4)
        sleep(2)
        #点击"立即加入"按钮
        self.click_buy_Buton()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'加入结果')))
        #点击返回按钮<，点4次，返回到理财页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()

        
    
    
    
        
        
#封装购买“理财金体验标”的整个过程--------------------------------------------------------------------------------------------------------------------------------------------------------
    
    #定位“理财金体验标”项目
    def financial_experience_project(self):
        return self.by_name("理财金体验标")
    
    #点击“理财金体验标”项目
    def click_financial_experience_project(self):
        self.financial_experience_project().click()
        
    #定位第一个单选框
    def checkbox_Button(self):
        return self.by_ids("com.xiaoniu.finance:id/checkbox")[0]
    
    #点击第一个单选框
    def click_checkbox_Button(self):
        self.checkbox_Button().click()
        
    #定位“确认购买”按钮
    def confirm_buy_Button2(self):
        return self.by_name("确认购买")
    
    #点击“确认购买”按钮
    def click_confirm_buy_Button2(self):
        self.confirm_buy_Button2().click()
        
    
        
        
    #封装“理财金体验标”的购买方法
    def buy_financial_experience_project(self):
        #向上滑动
        self.swipe('up',100)
        #点击进入理财金体验标的页面
        self.click_financial_experience_project()
        #点击第一个标，进入"理财金体验标"购买页面    
        self.click_project_list_choose_first()
        sleep(3)
        self.click_buy_Buton()
        self.click_checkbox_Button()
        self.click_confirm_buy_Button2()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,'购买结果')))
        #点击返回按钮<，点4次，返回到项目分类页面
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        loginPage.LoginPage(self.driver).click_back_Button()
        #向下滑动一下
        self.swipe('up',100)

    
    
        
        
        