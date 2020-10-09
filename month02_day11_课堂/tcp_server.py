"""
tcp 服务端基础示例
"""
from socket import *

# 创建tcp套接字 (默认也是tcp)
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(('0.0.0.0',8888))

# 设置监听
tcp_socket.listen(5)

# 等待处理客户端连接
print("Waiting for connect...")
connfd,addr = tcp_socket.accept()
print("Connect from,",addr) # 打印客户端地址

# 等待接收
data = connfd.recv(1024)
print("Recv:",data.decode())

# 都要关闭
connfd.close()
tcp_socket.close()