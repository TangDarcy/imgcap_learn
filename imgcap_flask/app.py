from flask import Flask,jsonify
from user import User

app = Flask(__name__)

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


@app.route('/')
def hello_world():
    user=User()
    arrData=user.get_user_info()
    return jsonify(arrData)


if __name__=="__main__":
    app.run(debug=True)