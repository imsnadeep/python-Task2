import datetime,time
from multiprocessing import Process
import os

class ParallelProcess():
    def __init__(self):
        pass
    
    def sequenceTraverse(self,*module):
        self.module = module
        print("start time for sequenceTraverse",datetime.datetime.now(),end="\n")
        for i in module[0]:
            print(i)
            
        print("End time for sequenceTraverse",datetime.datetime.now(),end="\n")
            
    def listTraverse(self,*module):
        start_time = time.time()
        print("PID for process 1:",os.getpid(),end="\n")
        print("start time in listTraverse:",start_time)
        for i in module:
            time.sleep(2)
            print("T1:",i)
        print("total time:",time.time()-start_time)
    
    def revTraverse(self,*module):
        self.module = module
        print("PID for process 2:",os.getpid(),end="\n")
        for i in module[::-1]:
            time.sleep(2)
            print("T2:",i)
            
clsObj=ParallelProcess()
clsObj.sequenceTraverse(["dut1","dut2","dut3","dut4"])

if __name__ == "__main__":
    p1 = Process(target=clsObj.listTraverse, args=(["dut1","dut2","dut3","dut4"]))
    p2 = Process(target=clsObj.revTraverse,args=(["dut1","dut2","dut3","dut4"]) )
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    print("done",end=" ")