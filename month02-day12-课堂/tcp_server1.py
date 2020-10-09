"""
tcp 服务端循环模型1
重点代码
"""

from socket import *

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
        data = connfd.recv(5)
        # 另外一端不存在了，recv会返回空字节
        if not data:
            break
        print("Recv:",data.decode())
        connfd.send(b"Thanks#")
    connfd.close() # 某个客户端退出对应的连接套接字就没用了

# 都要关闭
tcp_socket.close()


