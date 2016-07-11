#coding=UTF-8

'''
Created on 2015年12月21日

@author: wubingbing
'''

from unittest import TestCase
 
class CMethod(TestCase):
     
    def __init__(self):
        self._type_equality_funcs = {}
        
        
    #文本断言   
    def assertText(self,first,second):
        #firstS=first.encode('UTF-8')
        #secondS=second.encode('UTF-8')
        self.assertEqual(first,second)