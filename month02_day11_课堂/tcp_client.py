"""
tcp简单客户端演示
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket()

# 发起连接 连接服务端
tcp_socket.connect(("127.0.0.1",8888))

# 发送消息
msg = input(">>")
tcp_socket.send(msg.encode()) # 发送字节串

tcp_socket.close()