#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from appium import webdriver

class MyDriver:
    
    def Driver(self):
        capabilities = { 'platformName':'Android',
                        'platformVersion':'4.4.4',
                        'deviceName':'YQ601',
                        'appPackage':'com.xiaoniu.finance',
                        'appActivity':'.ui.LaucherTaskActivity',
                        'appWaitActivity':'.ui.MainActivity',
                        'unicodeKeyboard':'true',
                        'resetKeyboard':'true'}
        driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        return driver