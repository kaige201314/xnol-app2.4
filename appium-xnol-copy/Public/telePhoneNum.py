#coding=utf-8
'''
@author: wubingbing
'''

import random

class TelePhoneNum:
    
    def phoneNum(self):
        PhoneNum=random.choice(['130','186','189'])+''.join(random.choice('0123456789') for i in range(8))
        return PhoneNum
    

