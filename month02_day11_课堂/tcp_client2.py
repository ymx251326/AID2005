"""
tcp循环模型客户端1
重点代码
"""

from socket import *

# 发送消息
while True:
    msg = input(">>")
    if not msg:
        break
    # 创建tcp套接字
    tcp_socket = socket()
    # 发起连接 连接服务端
    tcp_socket.connect(("127.0.0.1", 8888))
    tcp_socket.send(msg.encode()) # 发送字节串
    data = tcp_socket.recv(1024)
    print("From server:",data.decode()) # 转换字符串
    tcp_socket.close()