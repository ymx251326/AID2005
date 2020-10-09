"""
GIL问题的效率测试
"""

import time
# from multiprocessing import Process
from threading import Thread

# 球函数运行时间
def timeis(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("执行时间:",end_time - start_time)
        return res
    return  wrapper

# 判断一个数是不是质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

class Prime(Thread):
    def __init__(self,begin,end):
        """
        :param begin: 开始数值
        :param end: 结尾数值
        """
        self.begin = begin
        self.end = end
        super().__init__()

    def run(self):
        prime = []
        for i in range(self.begin,self.end):
            if isPrime(i):
                prime.append(i)
        print(sum(prime))

@timeis
def thread_4():
    jobs = []
    for i in range(1,100001,25000):
        t = Prime(i,i+25000)
        jobs.append(t)
        t.start()
    for i in jobs:
        i.join()

thread_4() # 执行时间: 25.253902673721313

# @timeis
# def process_4():
#     jobs = []
#     for i in range(1,100001,25000):
#         p = Prime(i,i+25000)
#         jobs.append(p)
#         p.start()
#     for i in jobs:
#         i.join()
#
# process_4() # 执行时间: 14.229238033294678

