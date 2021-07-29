import multiprocessing
import time

#进程执行函数
def func():
    print("开始运行第一个进程喽")
    time.sleep(2)
    print("完成事情结束喽")

#实例化进程对象
p = multiprocessing.Process(target=func,name="aid",daemon=False)
p.start()
print(p.name)
print(p.pid)
print(p.is_alive())