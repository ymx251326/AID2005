"""
1. 上传头像 （图片自己找）

从客户端指定一张图片，将其传输到服务端
在服务端以 日期为图片名称存储

比如： 客户端有一张  xxxxx.jpg
 传到服务端存为   2020-7-10.jpg

 思路 ：　建立网络连接，　收图片
 1. 建立ｔｃｐ套接字
 ２．等待客户端连接
 3.接收图片内容
 4.将图片内容保存，以日期命名
 5. 接收完毕退出

"""
from socket import *
import time

# 建立ｔｃｐ套接字
sock = socket()
sock.bind(('0.0.0.0',8888))
sock.listen(5)

# 等待客户端连接
connfd,addr = sock.accept()
print("Connect from",addr)

filename = "%d-%d-%d.jpg"%time.localtime()[:3]
f = open(filename,'wb')
# 接收图片内容
while True:
    data = connfd.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
connfd.close()
sock.close()



