"""
思路：
1. 创建套接字
2. 连接服务端
3. 读取图片内容
4. 发送图片内容
5. 发送完成关闭
"""
from socket import *

# 创建套接字
sock = socket()

# 连接服务端
sock.connect(('127.0.0.1',8888))

# 读取图片内容
f = open("zly.jpg",'rb')

while True:
    data = f.read(1024)  # 字节串
    # 到文件结尾结束循环
    if not data:
        break
    # 发送图片内容
    sock.send(data)

# 关闭
f.close()
sock.close()


