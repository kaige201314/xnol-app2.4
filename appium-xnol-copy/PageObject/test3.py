#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


PhoneNO='222222'
print PhoneNO+"————这是mobileNo，即将写入PhoneNO.txt文件中去"
fout=open('PhoneNO.txt','w')
fout.write(PhoneNO)
fout.close()
print PhoneNO+"————这是mobileNo，已经写入PhoneNO.txt文件中了" 