"""
udp套接字演示 客户端
重点代码
"""
from socket import *

# 确定服务端地址
ADDR = ('127.0.0.1',8888)

# 创建套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)


# 循环发送接收消息
while True:
    msg = input(">>")
    # 空字符串执行break
    if not msg:
        break
    udp_socket.sendto(msg.encode(),ADDR)
    # 客户端结束
    # if msg == "##":
    #     break
    data,addr = udp_socket.recvfrom(1024)
    print("From server:",data.decode())

udp_socket.close()


