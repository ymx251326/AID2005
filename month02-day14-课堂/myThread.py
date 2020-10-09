"""
自定义线程类演示
"""
from threading import Thread
import time

class MyThread(Thread):
    def __init__(self,song):
        self.song = song
        super().__init__() # 加载父类属性

    def run(self):
        for i in range(3):
            print("Playing %s:%s"%(self.song,time.ctime()))
            time.sleep(2)

t = MyThread("小幸运")
t.start() # run作为线程执行
t.join()
