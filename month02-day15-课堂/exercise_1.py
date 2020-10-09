"""
练习1：  一个线程打印1--52  另一个线程打印A--Z
        两个线程一起启动，要求打印的结果
        12A34B56C.....5152Z

        提示: 使用同步互斥方法控制线程执行
              程序中不一定只有一个锁
"""
from threading import Thread,Lock

lock1 = Lock()
lock2 = Lock()

def print_num():
    # 每次循环打印2个数字
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i+1)
        lock2.release()

def print_char():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release()

t1 = Thread(target=print_num)
t2 = Thread(target=print_char)

lock2.acquire() # 让数字先执行

t1.start()
t2.start()
t1.join()
t2.join()




