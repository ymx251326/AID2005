"""
 写一个程序，使用udp。
要求，从客户端可以循环的输入单词，服务端查询到单词，讲
单词的解释发送给客户端，让客户端打印

单词通过数据表words查询

思路： 客户端输入一个单词，发送一次，然后等接收，打印
    服务端，接收单词，查询单词 将解释发送给客户端
"""
from socket import *
import pymysql

# 确定服务器地址
ADDR = ('0.0.0.0', 8888)

# 连接数据库-》创建游标——》执行sql-》查询结果
class Database:
    def __init__(self):
        self.db = pymysql.connect(user="root",
                                  password="123456",
                                  database="dict",
                                  charset="utf8")
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def find_word(self,word):
        """
        :param word: 要查询的单词
        :return: str 查询得到的解释  or Not Found
        """
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql,[word])
        result = self.cur.fetchone() # (mean,) None
        if result:
            return result[0] # 返回解释
        else:
            return "Not Found"

# 单词的接收和解释发送
def main():
    # 创建udp套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    # 绑定地址
    udp_socket.bind(ADDR)

    db = Database() # 生成数据库对象
    while True:
        # 接收单词
        word, addr = udp_socket.recvfrom(1024)
        # 查询单词
        result = db.find_word(word.decode())

        udp_socket.sendto(result.encode(), addr)  # 给对应客户端发送消息
    db.close()
    udp_socket.close()


if __name__ == '__main__':
    main() # 启动






