from multiprocessing import Process
import os

def runpp(fns):
    proc = []
    for fn in fns:
        p = Process(target=os.system(fn))
        p.start()
        proc.append(p)
    for q in proc:
        q.join()
    
    
md = ['s', 'i', 'q']
ty = ['s', 'c', 'r']
num = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 500000, 1000000, 10000000, 100000000, 1000000000]
Call = []

    
for m in md:
    for t in ty:
        for n in num:
           Call.append("python project1.py "+m+" "+str(n)+" "+t)           

if __name__ == '__main__':
    runpp(Call)
