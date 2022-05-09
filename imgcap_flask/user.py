from pymysql import connect
from pymysql.cursors import DictCursor

class User(object):
    def __init__(self):
        self.conn= connect(
            host='192.168.31.153',
            port=3306,
            user='tang',
            password='Root123!',
            database='image_system',
            charset='utf8'
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