"""
进程创建过程
1. 将需要新进程执行的事件封装为函数
2. 通过模块的Process类创建进程对象，关联函数
3. 通过进程对象调用start启动进程
4. 通过进程对象调用join回收进程资源
"""

import multiprocessing
from time import sleep

a = 10

# 进程执行函数
def fun():
    print("开始执行进程函数。。。")
    global a
    print("a =",a)
    a = 10000
    sleep(2)
    print("进程函数执行完了")

# 创建进程对象
p = multiprocessing.Process(target=fun)

# 启动进程 进程诞生，执行fun函数内容
p.start()

print("原来的进程做点事")
sleep(3)
print("事情干完了")

# 等待执行完后回收
p.join()
print("a:",a)
