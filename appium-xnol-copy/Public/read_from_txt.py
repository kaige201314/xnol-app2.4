#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os

class Read_from:
    
    def read_from(self,txtName):
        p="Data/"+txtName+""
        txtName_url=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, p))
        f=open(txtName_url)
        keyword=f.readlines()[0]
        print keyword+"------这是读取自"+txtName+""
        f.close()
        return keyword
