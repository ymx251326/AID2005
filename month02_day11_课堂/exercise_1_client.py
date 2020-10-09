from socket import *

# 确定服务端地址
ADDR = ('127.0.0.1',8888)

# 创建套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 循环发送接收消息
while True:
    # 输入单词
    word = input(">>")
    if not word:
        break
    # 发送单词
    udp_socket.sendto(word.encode(),ADDR)
    data,addr = udp_socket.recvfrom(1024)
    print("%s:%s"%(word,data.decode()))

print("退出程序")
udp_socket.close()


