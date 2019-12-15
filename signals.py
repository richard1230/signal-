

from blinker import Namespace
from datetime import datetime
from flask import  request,g

#定义信号
namespace = Namespace()
login_signal = namespace.signal('login')


#监听信号
def login_log(sender):
    now = datetime.now()
    ip = request.remote_addr
    log_line = "{username}*{now}*{ip}".format(username=g.username,now=now,ip=ip)
    with open('login_log.txt','a') as fp:
        fp.write(log_line+"\n")

    print('用户登录了')


login_signal.connect(login_log)

