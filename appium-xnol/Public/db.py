#coding=UTF-8

'''
@author: wubingbing
'''
import MySQLdb

class Db:
    def __init__(self,database):
        self.conn=MySQLdb.connect(
            host='172.20.20.230',
            port =3306,
            user='root',
            passwd='123456',
            db = database,
            charset='utf8'
            )
        
        
    def sql(self,sqlStr):   
        cur =self.conn.cursor()
        cur.execute(sqlStr)
        for row in cur.fetchall():    
            for r in row:    
                return r
        cur.close()
        self.conn.close()

