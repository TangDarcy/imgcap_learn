from flask import Flask,jsonify
from user import User
from flask_cors import *

app = Flask(__name__)

CORS(app,supports_credentials = True)
"""
接口说明：
1.返回json数据
2.结构：
{
    resCode: 0 ,非0即错
    data: 一般为数组
    message:"对本次请求的说明"
}
"""
app.config['JSON_AS_ASCII'] = False #解决中文乱码

login_code_dic={-1:"用户不存在",0:"登录成功",1:"密码错误"}

# @app.route('/')
# def hello_world():
#     user=User()
#     arrData=user.get_user_info()
#     userName="Tang"
#     passWord="tang123"
#     # userName="Qian"
#     login_code=user.is_login(userName,passWord)
#     print(login_code_dic[login_code])
#     return jsonify(login_code_dic[login_code])

@app.route('/login',methods=['POST'])
def user_login():
    data=request.get_json(silent=True)
    userName=data["userName"]
    passWord=data["passWord"]
    user=User()
    login_code=user.is_login(userName,passWord)
    return jsonify(login_code_dic[login_code])




if __name__=="__main__":
    app.run(debug=True)