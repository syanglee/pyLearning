from multiprocessing import Pool, cpu_count
import time

class MyPool(object):    
    def __init__(self):
        pass

    def func_1(self,a):
        time.sleep(1)
        return (a, a*a)
    
    def func_2(self,a,b):
        time.sleep(0.3)
        return (a+b, a*b)
    
    def main(self):
        begin = time.time()
        print('CPU核的数量：',cpu_count())
        with Pool(cpu_count()) as p:
            for i in range(8):
                result = p.apply(self.func_2,(1,i,))
            p.close()
            p.join()
        during = time.time() - begin
        print("func_2 result = ",result)
        print("apply during time: ", during)

    def main2(self):
        results = []
        begin = time.time()
        print('CPU核的数量：',cpu_count())
        with Pool(cpu_count()) as p:
            for i in range(8):
                result = p.apply_async(self.func_2,(1,i,))
                results.append(result)                
            p.close()
            p.join()
        during = time.time() - begin
        # pool.apply_async()之后的语句都是阻塞执行的，调用 result.get() 会等待上一个任务执行完之后才会分配下一个任务。
        # 事实上，获取返回值的过程最好放在进程池回收之后进行，避免阻塞后面的语句。
        print("func_2 result = ",results[0].get()) 
        print("apply_async during time: ", during)  # apply_async()方法比apply()执行的速度快很多

if __name__ == "__main__":
    mp = MyPool()
    mp.main()