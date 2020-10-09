"""
tcp 服务端循环模型 2
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
print("处理客户端消息")
while True:
    connfd,addr = tcp_socket.accept() # 连接客户端
    print("Connect from",addr) # 打印客户端地址
    data = connfd.recv(1024)
    print("Recv:",data.decode())
    connfd.send(b"Thanks")
    connfd.close() # 某个客户端退出对应的连接套接字就没用了

# 都要关闭
tcp_socket.close()


