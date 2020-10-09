"""
进程属性设置演示
"""
from multiprocessing import Process
import time

def fun():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)

# 创建进程
p = Process(target = fun,name = "print_time")

# 该子进程会随父进程退出而退出  在start前
p.daemon = True

p.start() # 进程启动

print("p.name:",p.name)
print("p.pid:",p.pid)
print("p.is_alive:",p.is_alive())