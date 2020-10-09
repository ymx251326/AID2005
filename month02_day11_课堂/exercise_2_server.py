"""
练习1：  使用tcp完成 模拟客服机器人对话
小美    你多大了 --》 我2岁啦；
       你是男生女生 --》 我是机器人，没有性别之分啦
       xxx --> xxxxx

从客户端可以不断的发送问题，小美会将回答发送回答打印，如果你的问题
它听不懂则回复 "人家还小不太明白"。
"""

from socket import *

# 对话字典
chat = {"你好":"你好",
        "叫什么":'我叫小美啊',
        "几岁":'我2岁啦',
        "男生女生":"我是机器人"
        }

# 创建tcp套接字 (默认也是tcp)
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(('0.0.0.0',8888))

# 设置监听
tcp_socket.listen(5)

# 循环等待处理客户端连接
while True:
    print("Waiting for connect...")
    connfd,addr = tcp_socket.accept()
    print("Connect from",addr) # 打印客户端地址

    # 等待接收
    while True:
        data = connfd.recv(1024)
        # 另外一端不存在了，recv会返回空字节
        if not data:
            break

        # 遍历字典
        for i in chat:
            # 找到对应问题则返回对应的值
            if i in data.decode():
                connfd.send(chat[i].encode())
                break
        else:
            # 没有找到问题
            connfd.send("人家还小，不太明白".encode())

    connfd.close() # 某个客户端退出对应的连接套接字就没用了

# 都要关闭
tcp_socket.close()


