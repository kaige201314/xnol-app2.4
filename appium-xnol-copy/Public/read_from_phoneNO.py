#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os

class Read_from_phoneNO:
    
    def read_phoneNO(self):
        p='Data/phoneNO.txt'
        #由于phoneNO.txt在Data目录下，与当前文件不再同一个目录，所以要先获取当前文件的绝对路径，然后拼接p
        #phoneNO_txt_url就是phoneNO.txt的绝对路径
        phoneNO_txt_url=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, p))
        #读取phoneNO.txt得到刚刚上一用例中注册用户成功后的手机号，作为登录的用户名
        fin=open(phoneNO_txt_url)
        phoneNO=fin.readlines()[0]
        print phoneNO+"————mobileNo，这就是即将要***的账户手机号"
        fin.close()
        return phoneNO        
