"""
非阻塞IO
套接字对象 --》 非阻塞
"""
from socket import *
import time

# 打开日志文件
f = open("my.log",'a')

# 创建tcp套接字
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

# 设置套接字的非阻塞
# sockfd.setblocking(False)

# 超时检测时间
sockfd.settimeout(3)

while True:
    print("Waiting for connect")
    try:
        connfd,addr = sockfd.accept() # 阻塞等待
        print("Connect from",addr)
    except BlockingIOError as e:
        # 干点别的事
        msg = "%s : %s\n"%(time.ctime(),e)
        f.write(msg)
        time.sleep(2)
    except timeout as e:
        # 干点别的事
        msg = "%s : %s\n"%(time.ctime(),e)
        f.write(msg)
    else:
        # 正常有客户端连接
        data = connfd.recv(1024)
        print(data.decode())


