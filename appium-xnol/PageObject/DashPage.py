#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import BasePage
from BasePage import BaseAction
from appium.webdriver.common.touch_action import TouchAction

'''
小牛在线app2.2首页涉及的所有页面元素操作方法——>封装
'''
driver = webdriver.Remote('http://localhost:4723/wd/hub', BasePage.BaseAction.capabilities)

#首页定位，即第一个主页面
firstPage_loc=(By.XPATH,"//android.widget.CheckBox[contains(@text,'首页')]")
#理财页定位，即第二个主页面
secondPage_loc=(By.XPATH,"//android.widget.CheckBox[contains(@text,'理财')]")
#发现定位，即第三个个主页面
thirdPage_loc=(By.XPATH,"//android.widget.CheckBox[contains(@text,'发现')]")
#我的页定位，即第四个主页面
forthPage_loc=(By.XPATH,"//android.widget.CheckBox[contains(@text,'我的')]")
#登录用户的账户名称定位
accountName_loc=(By.ID,"account_name")
#手势密码定位
gesture_loc=(By.CLASS_NAME,"android.view.View")
#登录链接定位
login_loc=(By.ID,"com.xiaoniu.finance:id/account_no_login")
#登录页面输入框定位
loginPage_input_loc=(By.CLASS_NAME,"android.widget.EditText")
#登录按钮定位
loginPage_button_loc=(By.XPATH,"//android.widget.Button[contains(@text,'登录')]")
#当前页面标题定位
currentPageTitleName_loc=(By.ID,"com.xiaoniu.finance:id/titlebar_tv_center")

class Dash(BasePage.BaseAction):  

    
    #定义recover返回函数，keyevent(number)的作用相当于Android实体机的返回键，number代表点击返回键的次数
    def recover(self):
        while True:
            try:
                if len(self.driver.find_element(By.XPATH,"//android.widget.CheckBox")): 
                    break
            except:
                self.driver.keyevent(4)
    
    #手势滑动的单步操作        
    def from_to(self,start_el,end_el):
        TouchAction(self.driver).press(start_el).move_to(end_el).perform()
                
    #定义手势操作方法，须传入至少4个位置参数（loc_list是一个list，包含至少4个值）
    def gesture(self,loc_list):
        el=self.driver.find_element(By.CLASS_NAME,"android.view.View")
        n=0
        for x in loc_list:
            self.from_to(el[loc_list[n]],el[loc_list[n+1]])
            n=n+1


    

        
    #获取当前页面标题
    def getCurrentPageTitle(self):
        PageTitleName=self.driver.find_elements(By.ID,"com.xiaoniu.finance:id/titlebar_tv_center")[0].text
        #print PageTitleName
        return PageTitleName   
    
    
    #获取当前登录的用户的账户名称
    def getCurrentAccountName(self):
        #首先返回"我的"页面，在“我的”页面可以获取到账户名称ID，以此可以获得用户的账户名称        
        Dash(driver).recover()
        self.driver.find_element(By.XPATH,"//android.widget.CheckBox[contains(@text,'我的')]").click()
        time.sleep(1)
        #获取当前的用户名
        account_name=self.driver.find_element(By.ID,"account_name").text
        return account_name
    
            

   
        
       

