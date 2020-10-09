"""
练习2 ： 拷贝一个目录
编写程序完成，将一个文件夹拷贝一份
* 假设文件夹中只有普通文件
* 将每个文件的拷贝作为一个拷贝事件
* 使用进程池完成事件

提示 ： os.mkdir('name')
"""
from multiprocessing import Pool,Queue
import os,sys

q = Queue() # 创建消息队列

# 拷贝一个文件
def copy(file,old_folder,new_folder):
    fr = open(old_folder+'/'+file,'rb')
    fw = open(new_folder+'/'+file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data) # 写入多少就是拷贝多少
        q.put(n) # 放入消息队列
    fr.close()
    fw.close()

# 获取文件夹大小
def get_size(dir):
    total_size = 0
    for file in os.listdir(dir):
        total_size += os.path.getsize(dir+'/'+file)
    return total_size

# 使用进程池
def main():
    old_folder = input("你要拷贝的目录:")
    # 文件夹大小
    total_size = get_size(old_folder)
    new_folder = old_folder + "-备份"
    try:
        os.mkdir(new_folder)
    except:
        sys.exit("该目录已存在")

    # 创建进程池
    pool = Pool()
    # 遍历目录，确定要拷贝的文件
    for file in os.listdir(old_folder):
        pool.apply_async(func=copy,args=(file,old_folder,new_folder))

    copy_size = 0
    while copy_size < total_size:
        copy_size += q.get() # 从消息队列获取数值累加
        print("拷贝了 %.2f%%"%(copy_size/total_size*100))


    pool.close()
    pool.join()

if __name__ == '__main__':
    main()