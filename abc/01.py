import multiprocessing
import time

#进程执行函数
def func():
    print("开始运行第一个进程喽")
    time.sleep(2)
    print("完成事情结束喽")

#实例化进程对象
p = multiprocessing.Process(target=func)
#启动进程 此刻产生进程，运行func函数
p.start()

print("我也要做点事情")
time.sleep(3)
print("我也做完喽")

#阻塞等待回收进程
p.join()