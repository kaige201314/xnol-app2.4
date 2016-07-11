#coding=utf-8
'''
@author: wubingbing
'''
import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from db import Db
from appium.webdriver.common.touch_action import TouchAction
from cMethod import CMethod

class Common:
    
    
    
    def __init__(self,driver):
        self.driver=driver
        
        
    
    def recover(self):

        while True:
            try:
                if self.driver.find_element_by_name('首页'): 
                    break
            except:
                self.driver.keyevent(4)

                
        
    def getVercode(self,teleNum):
        time.sleep(5)
        content=Db("xnmsg").sql("SELECT content FROM sms_sendlog_his WHERE mobile="+teleNum+" ORDER BY id DESC LIMIT 1 ")
        code_zc=filter(str.isdigit,content.encode('UTF-8'))
        return code_zc
        print code_zc

    def getSize(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return(x,y)
    
    def swipeLeft(self,t):
        l=self.getSize()
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.25)
        self.driver.swipe(x1,y1,x2,y1,t)
        
    def swipeRight(self,t):
        l=self.getSize()
        x1=int(l[0]*0.25)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.75)
        self.driver.swipe(x1,y1,x2,y1,t)
        
    def swipeUp(self,t):
        l=self.getSize()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.75)
        y2=int(l[1]*0.25)
        self.driver.swipe(x1,y1,x1,y2,t)

        
    def swipeDown(self,t):
        l=self.getSize()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.25)
        y2=int(l[1]*0.75)
        self.driver.swipe(x1,y1,x1,y2,t)
    
    
    #绘制手势密码L
    def gesture(self):
        el=self.driver.find_elements_by_class_name('android.view.View')
        TouchAction(self.driver).press(el[0]).move_to(el[1]).move_to(el[4]).move_to(el[7]).move_to(el[8]).release().perform()
         
        
        
    #以下是xxk增加的函数
    #登录函数
    def userLogin(self,username,password):
        driver=self.driver
        #首先返回"我的"页面，此步要在调用本函数前实现
        Common(driver).recover()
        driver.find_element_by_id("com.xiaoniu.finance:id/account_no_login").click()
        time.sleep(2)
        #定义输入框list
        #inputList=driver.find_elements_by_class_name("android.widget.EditText")
        driver.find_elements_by_class_name("android.widget.EditText")[0].clear()
        driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys(username)
        driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys(password)
        driver.find_element_by_name("登录").click()
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.NAME,'邱君华')))
        #acountName = driver.find_element_by_id("com.xiaoniu.finance:id/account_name").text
        #driver.assertEqual(acountName,u"邱君华",u"登录失败……")
        #time.sleep(3)
        
                
    #获取页面标题
    def getitemPageName(self):
        itemPageName1=self.driver.find_elements_by_id('com.xiaoniu.finance:id/titlebar_tv_center')[0].text
        print itemPageName1
        return itemPageName1    
        
 
    #取得当前登录的用户名
    def getUserName(self):
        #首先返回"我的"页面，此步要在调用本函数前实现
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        time.sleep(1)
        #获取当前的用户名
        username=self.driver.find_element_by_id('account_name').TEXT
        return username
    
        
        
    #查询理财师页面的昨日奖励
    def getAmount_Yesterday_Value(self,username):
        driver=self.driver
        time.sleep(5)
        Earnings=Db().sql("select earnings from t_fp_earnings_day where plannerId in(SELECT id from t_user t where t.username='username') and state=1 and TO_DAYS(NOW())-TO_DAYS(earningDate)=1")
        time.sleep(5)
        print Earnings
        return Earnings

            
        
    #查询理财师页面的累计奖励
    def get_Amount_Allapraise_Value(self,username):
        driver=self.driver
        oldEarnings=Db().sql("select SUM(old.earnings) as total1 from t_fp_earnings old where plannerId in(SELECT id from t_user t where t.username='username') and state=1")
        time.sleep(5)
        newEarnings=Db().sql("select SUM(new.earnings) as total1 from t_fp_earnings_day new where plannerId in(SELECT id from t_user t where t.username='username') and state=1")
        time.sleep(5)
        allEarnings=oldEarnings+newEarnings
        print allEarnings
        return allEarnings
                

        
        
    #查询理财师页面，当前用户已邀请好友总数量
    def getInviste_Allfriend_Num(self,username):
        driver=self.driver
        time.sleep(5)
        #friendNumber=Db().sql("select count(*) from t_fp_relationship where plannerId in(SELECT id from t_user t where t.username="username")")
        time.sleep(5)
        
    #查询好友统计页面，当前用户邀请的"注册人数"
    
    
    #查询好友统计页面，当前用户邀请的"实名人数"
    
    
    #查询好友统计页面，当前用户邀请的"已投资人数"
    
    
    #查询好友统计页面，好友推荐的好友邀请的"注册人数"
    
    
    #查询好友统计页面，好友推荐的好友邀请的的"实名人数"
    
    
    #查询好友统计页面，好友推荐的好友邀请的的"已投资人数"
    
        
        
    #查询理财师页面的分享现金红包
    def getCash_bonus(self,username):
        driver=self.driver
        time.sleep(5)
        CashBonus=Db().sql("select balance from cash_bonus_send where userId in(SELECT id from t_user t where t.username='username') and bonusStatus=1")
        return CashBonus
    
        

        
    
        
        