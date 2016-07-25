#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Write_to_PhoneNO:

    #将自动生成的手机号写入PhoneNO.txt文件
    def write_to_PhoneNO(self,PhoneNO):
        print PhoneNO+"————这是mobileNo，即将写入PhoneNO.txt文件中去"
        fout=open('PhoneNO.txt','w')
        b=''.join(PhoneNO)
        fout.write(b)
        fout.close()
        print PhoneNO+"————这是mobileNo，已经写入PhoneNO.txt文件中了" 