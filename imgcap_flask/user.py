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
        # print(userName)
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
    #判断用户是否存在
    def is_user_exist(self,userName):
        sql="""select username from i_user where username='{}'""".format(userName)
        self.cursor.execute(sql)
        data=[]
        for temp in self.cursor.fetchall():
            data.append(temp)
        if len(data)==0:
            return False
        return True
    #注册新用户,完成注册后返回0
    def is_register(self,userName,passWord,age,sex,email,telephone):
        sql="insert into i_user(username,password,age,sex,email,tel) values(%s,%s,%s,%s,%s,%s)"
        param=(userName,passWord,age,sex,email,telephone)
        try:
            self.cursor.execute(sql,param)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            return -1
        return 0
    def get_userInfo_Byname(self,userName):
        sql="""select username,age,sex,email,tel from i_user where username='{}'""".format(userName)
        self.cursor.execute(sql)
        data=[]
        for temp in self.cursor.fetchall():
            data.append(temp)
        if len(data)==0:
            return -1
        if data[0]["sex"]=="man":
            sex="男"
        else:
            sex="女"
        user_info={
            'userName': data[0]["username"],
            'age': data[0]["age"],
            'sex': sex,
            'email': data[0]["email"],
            'telephone': data[0]["tel"],
        }
        return user_info
    #修改用户信息
    def change_userInfo(self,userName,age,sex,email,telephone):
        sql="update i_user set age=%s,sex=%s,email=%s,tel=%s where username=%s"
        param=(age,sex,email,telephone,userName)
        try:
            self.cursor.execute(sql,param)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            return -1
        return 0
    #修改密码
    def change_pwd(self,userName,oldPwd,newPwd):
        sql="""select username,password from i_user where username='{}'""".format(userName)
        self.cursor.execute(sql)
        data=[]
        for temp in self.cursor.fetchall():
            data.append(temp)
        if len(data)==0:
            return -1
        elif data[0]["password"]!=oldPwd:
            print(data[0]["password"])
            return -2        
        sql="update i_user set password=%s where username=%s"
        param=(newPwd,userName)
        try:
            self.cursor.execute(sql,param)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            return -1
        return 0    
