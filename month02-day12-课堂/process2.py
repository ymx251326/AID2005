"""
包含参数的进程函数演示
"""
from multiprocessing import Process
from time import sleep

# 带有参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

# 位置传参
# p = Process(target=worker,args=(2,"Levi"))

# 关键字传参
p = Process(target=worker,args=(2,),kwargs={"name":"Baron"})
p.start()

p.join(3)
print("=========================================")