#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os

class Read_from_activatronCode:
    
    def read_activatronCode(self):
        #读取activatronCode.txt文件的第一行作为激活码，然后删除第一行，保存第二行为第一行，保证每次读取的激活码为第一行的内容
        p='Data/activatronCode.txt'
        #由于activatronCode.txt在Data目录下，与当前文件不再同一个目录，所以要先获取当前文件的绝对路径，然后拼接p
        #activatronCode_txt_url就是activatronCode.txt的绝对路径
        activatronCode_txt_url=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, p))
        #读取activatronCode.txt中的第一行激活码，然后删除第一行，保存第二行为第一行，保证每次读取的激活码为第一行的内容
        fin=open(activatronCode_txt_url)
        activatronCodes=fin.readlines()
        activatronCode=activatronCodes[0]
        print activatronCode
        fout=open(activatronCode_txt_url,'w')
        b=''.join(activatronCodes[1:])
        fout.write(b)
        print activatronCode+'---------删除第一行，更新activatronCode.txt'
        fin.close()
        fout.close()
        return activatronCode