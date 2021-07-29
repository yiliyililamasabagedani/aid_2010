from multiprocessing import Process
import time

def worker(sec,name):
    for i in range(3):
        time.sleep(sec)
        print(f"i am {name}")
        print("i am working")

# p = Process(target=worker,args=(2,"Tom"))
p = Process(target=worker,args=(2,),kwargs={"name":"Joy"})
p.start()
p.join()
