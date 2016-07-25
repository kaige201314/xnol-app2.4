#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os

class Write_to:

    #将自动生成的手机号写入某个txt文件
    def write_to(self,key_word,txtName):
        p="Data/"+txtName+""
        txtName_url=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, p))
        f=open(txtName_url,'w')
        b=''.join(key_word)
        f.write(b)
        f.close()
        print key_word+"------已经写入到"+txtName+"文件中了"