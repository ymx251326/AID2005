"""
udp_server.py  udp套接字编程演示
重点代码
"""
from socket import *

# 确定服务器地址
ADDR = ('0.0.0.0',8888)

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
udp_socket.bind(ADDR)

while True:
    # 接收客户端消息
    msg,addr = udp_socket.recvfrom(1024)
    # 与客户端约定了一个特殊的退出指令 服务端程序一般不退出
    # if msg == b'##':
    #     break
    print("Recv:",msg.decode())
    udp_socket.sendto(b"Thanks",addr) # 给对应客户端发送消息

udp_socket.close()