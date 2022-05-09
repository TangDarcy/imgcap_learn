from pymysql import connect
from pymysql.cursors import DictCursor
from settings import MYHOST,MYPORT,MYUSER,MYPASSWORD,MYDATABASE
class User(object):
    def __init__(self):
        self.conn= connect(
            host= MYHOST,
            port= MYPORT,
            user= MYUSER,
            password= MYPASSWORD,
            database=MYDATABASE,
            charset= 'utf8'
        )
        self.cursor=self.conn.cursor(DictCursor)
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_user_info(self):
        sql='select * from i_user limit 1'
        self.cursor.execute(sql)
        
        data=[]
        for temp in self.cursor.fetchall():
            data.append(temp)
        
        return data