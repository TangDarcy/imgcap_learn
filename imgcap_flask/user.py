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
    
    def is_login(self,userName,passWord):#-1代表用户名不存在，0表示登录成功，1表示密码错误
        print(userName)
        sql="""select username,password from i_user where username='{}'""".format(userName) 
        self.cursor.execute(sql)
        data=[]
        for temp in self.cursor.fetchall():
            data.append(temp)
        if len(data)==0:
            return -1
        elif data[0]["password"]==passWord:
            return 0
        else:
             return 1
        return 1

