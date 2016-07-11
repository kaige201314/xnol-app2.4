#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
import time
import xlrd.sheet
import time, os

class BaseAction(object):
    """
    BasePage封装所有页面都公用的基础方法，例如:driver、find_element
    """
    
    driver = None
    capabilities = { 'platformName':'Android',
                     'platformVersion':'4.4.4',
                     'deviceName':'YQ601',
                     'appPackage':'com.xiaoniu.finance',
                     'appActivity':'.ui.LaucherTaskActivity',
                     'appWaitActivity':'.ui.MainActivity',
                     'unicodeKeyboard':True,
                     'resetKeyboard':True}
    


    def __init__(self,driver,capabilities):
        self.driver = driver
        
        
    
    #重新定义单个元素的定位方法
    def by_id(self, the_id):
        return self.driver.find_element_by_id(the_id)

    def by_name(self, the_name):
        return self.driver.find_element_by_name(the_name)
    
    def by_class_name(self,the_class_name):
        return self.driver.find_element_by_class_name(the_class_name)
    
    def by_xpath(self,the_xpath):
        return self.driver.find_element_by_xpath(the_xpath)

    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)
    
    
    #重新定义一组元素的定位方法
    def by_ids(self, the_id):
        return self.driver.find_element_by_id(the_id)

    def by_names(self, the_name):
        return self.driver.find_element_by_name(the_name)
    
    def by_class_names(self,the_class_names):
        return self.driver.find_element_by_class_name(the_class_names)
    
    def by_xpaths(self,the_xpath):
        return self.driver.find_element_by_xpath(the_xpath)

    def by_csss(self, css):
        return self.driver.find_element_by_css_selector(css)



    #重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)
    

     

            
            
    #定义获取屏幕宽度和高度的方法       
    def getSize(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return(x,y)
                        
    #封装页面滑动方法，须传入参数：方向direction和滑动时间t
    def swipe(self,direction,t):
        try:
            if direction == "left":
                l=self.getSize()
                x1=int(l[0]*0.75)
                y1=int(l[1]*0.5)
                x2=int(l[0]*0.25)
                self.driver.swipe(x1,y1,x2,y1,t)
            elif direction == "right":
                l=self.getSize()
                x1=int(l[0]*0.25)
                y1=int(l[1]*0.5)
                x2=int(l[0]*0.75)
                self.driver.swipe(x1,y1,x2,y1,t)
            elif direction == "up":
                l=self.getSize()
                x1=int(l[0]*0.5)
                y1=int(l[1]*0.75)
                y2=int(l[1]*0.25)
                self.driver.swipe(x1,y1,x1,y2,t)
            elif direction == "down":
                l=self.getSize()
                x1=int(l[0]*0.5)
                y1=int(l[1]*0.25)
                y2=int(l[1]*0.75)
                self.driver.swipe(x1,y1,x1,y2,t)
        except:
            print "%s 页面不能按指定的%s 方向滑动，请检查方向参数是否为上下左右！" %(self,direction)        
                
                



