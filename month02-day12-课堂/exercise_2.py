"""
练习1： 大文件拆分
将一个文件拆分为两个部分，每个部分分别是文件的一半
即源文件的上下半部分，分别拆到一个新文件里

要求使用两个进程同时进行

提示： 按照文件的字节数计算文件大小
      os.path.getsize()

思路： 获取图片的大小  上 下两个部分的拆分分别封装为函数
"""
from multiprocessing import Process
import os

size = os.path.getsize("zly.jpg")  # 获取文件大小

# 复制上半部分
def top():
    fr = open("zly.jpg", 'rb')
    fw = open("top.jpg", 'wb')
    n = size // 2  # 要拷贝n个字节
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()


# 复制下半部分
def bot():
    fr = open("zly.jpg",'rb')
    fw = open("bot.jpg", 'wb')
    fr.seek(size // 2, 0)  # 文件偏移量到中间
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

p = Process(target=top) #　子进程执行一个
p.start()
bot() # 父进程同时执行一个
p.join()
