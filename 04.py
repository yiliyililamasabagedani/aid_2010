from multiprocessing import Process
import time,os

size = os.path.getsize("zhao.png")

def top():
    fr = open("zhao.png","rb")
    fw = open("小欣.png","wb")
    n = size // 2
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()

def bottom():
    fr = open("zhao.png","rb")
    fw = open("小孙.png","wb")
    fr.seek(size // 2)
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

p = Process(target=top)
p.start()

bottom()
p.join()