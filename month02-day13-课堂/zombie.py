"""
演示僵尸进程
"""
from multiprocessing import Process
import os,time
from signal import *

def fun():
    for i in range(3):
        print(os.getpid())
        time.sleep(1)

# 父进程忽略子进程退出信号，由系统处理
signal(SIGCHLD,SIG_IGN)

# 创建进程
p = Process(target = fun,name = "print_time")
p.start()

while True:
    pass