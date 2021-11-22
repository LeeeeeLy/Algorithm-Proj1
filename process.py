import os
import multiprocessing

cores = multiprocessing.cpu_count()-2


sortOpt = ['s', 'i', 'q']
#dataType = ['s', 'c', 'r']
dataType = ['s', 'r']
#dataNumber = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 500000, 1000000, 10000000, 100000000, 1000000000]
dataNumber = [10000]
#dataNumber = [500000, 1000000, 10000000, 100000000, 1000000000]

commands = []

def sysCommandExe(command):
    os.system(command)


for sort in sortOpt:
    for data in dataType:
        for num in dataNumber:
            commands.append("python project1.py "+sort+" "+str(num)+" "+data)
if __name__ == '__main__':
    p = multiprocessing.Pool(cores)

    with p:
        p.map(sysCommandExe, commands)


