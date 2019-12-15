from flask import Flask,request,g
from blinker import Namespace

from signals import login_signal

# #定义信号
# zlspace = Namespace()
# fire_signal =zlspace.signal('fire')
#
# #监听信号
# def fire_bullet(sender):
#     print(sender)
#     print('start fire bullet')
# fire_signal.connect(fire_bullet)
#
#
# #发送一个信号
# fire_signal.send()



#定义一个登陆的信号
"""
以后用户登录进来，就发送一个登陆信号;
然后能够监听这个信号;
在监听到这个信号以后,就记录当前这个用户的信息；
用信号的方式记录用户的登陆信息
"""



app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/')
def login():
    #通过字符串查询的方式来传递字符串
    username = request.args.get('username')
    if username:
        g.username=username
        #发送信号
        login_signal.send()
        return '登陆成功'
    else:
        return '请输入用户名'



if __name__ == '__main__':
    app.run()
