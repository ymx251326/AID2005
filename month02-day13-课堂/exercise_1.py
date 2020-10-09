"""
练习1 ： 编写一个程序
* 使用单进程 求100000以内质数之和  记录所用时间
* 使用4个进程，将100000拆分为4份，分别求每部分中质数之和 记录时间
* 使用10个进程，将100000拆分为10份，分别求每部分中质数之和 记录时间
"""
import time
from multiprocessing import Process

# 求函数运行时间
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

# @timeis
# def no_process():
#     prime = []
#     for i in range(1,100001):
#         if isPrime(i):
#             prime.append(i) # 将质数加入列表
#     print(sum(prime))
#
# no_process() # 执行时间: 25.926925897598267

class Prime(Process):
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
# process_4() # 执行时间: 15.002186059951782

@timeis
def process_10():
    jobs = []
    for i in range(1,100001,10000):
        p = Prime(i,i+10000)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()

process_10() # 执行时间: 13.301548480987549