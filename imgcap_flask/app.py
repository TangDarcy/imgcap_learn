from flask import Flask,jsonify,request,session
from user import User
from flask_cors import *
from response_code import RESCODE
import datetime
app = Flask(__name__)
CORS(app,supports_credentials = True)
app.config['JSON_AS_ASCII'] = False #解决中文乱码
##用户登录
@app.route('/',methods=['POST'])
def user_login():
    userName = request.json.get('userName')
    passWord = request.json.get('passWord')
    # userName="Tang"
    # passWord=""
    user=User()
    if not all([userName,passWord]):
        return jsonify({'code':RESCODE.NULLDATA, 'msg':'用户名或密码不能为空'})
    login_code=user.is_login(userName,passWord)
    if login_code==-1:
        return jsonify({'code':RESCODE.NODATA, 'msg':'用户名不存在'})
    elif login_code==1:
        return jsonify({'code':RESCODE.ERRERDATA, 'msg':'密码错误'})
    elif login_code==0:
        return jsonify({'code':RESCODE.OK, 'msg':'登录成功','session':userName})
    return jsonify({'code':RESCODE.UNKONWERROR, 'msg':'error'})
#用户注册
@app.route('/register',methods=['POST'])
def user_register():
    user=User()
    userName = request.json.get('userName')
    if user.is_user_exist(userName):
        return jsonify({'code':RESCODE.USEREXIST,'msg':'用户已存在'})
    passWord = request.json.get('passWord')
    age=request.json.get('age')
    sex=request.json.get('sex')
    email=request.json.get('email')
    telephone=request.json.get('telephone')
    register_code=user.is_register(userName,passWord,age,sex,email,telephone) 
    if register_code==0:
        return jsonify({'code':RESCODE.OK, 'msg':'注册成功'})
    return jsonify({'code':RESCODE.UNKONWERROR, 'msg':'error'})
#获取用户信息
@app.route('/getUserInfo',methods=['POST'])
def get_userInfo():
    user=User()
    # print(request)
    userName=request.json.get('userName')
    user_info=user.get_userInfo_Byname(userName)
    if user_info==-1:
        return jsonify({'code':RESCODE.NODATA, 'msg':'用户不存在'})
    return jsonify({'code':RESCODE.OK,'msg':'返回用户信息','user_info':user_info})
#用户修改个人信息
@app.route('/changeInfo',methods=['POST'])
def userInfo_change():
    user=User()
    userName = request.json.get('userName')
    if user.is_user_exist(userName)==False:
        return jsonify({'code':RESCODE.USERNOTEXIST,'msg':'用户不存在'})
    age=request.json.get('age')
    sex=request.json.get('sex')
    email=request.json.get('email')
    telephone=request.json.get('telephone')
    changeinfo_code=user.change_userInfo(userName,age,sex,email,telephone) 
    if changeinfo_code==0:
        return jsonify({'code':RESCODE.OK, 'msg':'修改成功'})
    return jsonify({'code':RESCODE.UNKONWERROR, 'msg':'error'})
#用户修改密码
@app.route('/changePwd',methods=['POST'])
def userPwd_change():
    user=User()
    userName = request.json.get('userName')
    oldPwd = request.json.get('oldPwd')
    newPwd1 = request.json.get('newPwd1')
    newPwd2 = request.json.get('newPwd2')
    if user.is_user_exist(userName)==False:
        return jsonify({'code':RESCODE.USERNOTEXIST,'msg':'用户不存在'})
    if newPwd1!=newPwd2:
        return jsonify({'code':RESCODE.NEWPWDNOTSAME,'msg':'新密码输入不匹配'})
    if newPwd1==oldPwd:
        return jsonify({'code':RESCODE.PWDNOTCHANGE,'msg':'新旧密码不能相同'})
    changepwd_code=user.change_pwd(userName,oldPwd,newPwd1)
    if changepwd_code==0:
        return jsonify({'code':RESCODE.OK, 'msg':'修改成功'})
    elif changepwd_code==-2:
        return jsonify({'code':RESCODE.ERRORPWD, 'msg':'密码输入错误'})
    return jsonify({'code':RESCODE.UNKONWERROR, 'msg':'error'})
if __name__=="__main__":
    app.run(debug=True)