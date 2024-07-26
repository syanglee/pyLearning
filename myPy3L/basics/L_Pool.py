# 导入进程模块
import time
import psutil
from multiprocessing import Pool

"""
apply(func, args=(), kwds={})
该函数用于传递不定参数，主进程会被阻塞直到函数执行结束（不建议使用，并且3.x以后不再出现）

apply_async(func[, args=()[, kwds={}[, callback=None]]])
与apply用法一致，但它是非阻塞的且支持结果返回后进行回调

map(func, iterable, chunksize=None)
Pool类中的map方法，与内置的map函数用法基本一致，它会使进程阻塞直到结果返回

map_async(func, iterable, chunksize, callback)
与map用法一致，但是它是非阻塞的。其有关事项见apply_async

close()
关闭进程池（pool），使其不在接受新的任务

terminal()
结束工作进程，不在处理未处理的任务

join()
主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用

"""

def run(msg):
    print("开始：", msg)
    time.sleep(3)
    print("完成：", msg)

def double_it(i):
    return i * 2

if __name__ == "__main__":
    print("开始主程序")
    print("获取 CPU 的逻辑数量", psutil.cpu_count())
    print("获取 CPU 的物理核心数量", psutil.cpu_count(logical=False))
    # 使用进程池创建子进程
    size = 3
    # 这里设置允许同时运行的的进程数量要考虑机器cpu的数量，进程的数量最好别小于cpu的数量，
    # 因为即使大于cpu的数量，增加了任务调度的时间，效率反而不能有效提高
    pool = Pool(processes = size)

    for i in range(size):
        msg = "同步阻塞子进程 %s" %i
        msg_async = "异步不阻塞子进程 %s" %i
        start_time=time.time()
        # apply是阻塞的
        # 首先主进程开始运行，碰到子进程，操作系统切换到子进程，
        # 等待子进程运行结束后，再切换到另外一个子进程，直到所有子进程运行完毕。
        # 然后在切换到主进程，运行剩余的部分。
        #pool.apply(run,(msg,))

        # apply_async是异步非阻塞的
        # 不用等待当前进程执行完毕，
        # 随时根据系统调度来进行进程切换首先主进程开始运行，
        # 碰到子进程后，主进程说：让我先运行个够，等到操作系统进行进程切换的时候，再交给子进程运行。
        #pool.apply_async(run,(msg_async,))
        
    print("主进程结束耗时 %s" %(time.time() - start_time))

    s2_time = time.time()
    
    # 
    result = pool.map(double_it,range(10))

    pool.close()
    # 调用join之前，先调用close函数，否则会出错。
    # 执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    pool.join()

    print("result = ", result)

    print("计算用时：", time.time() - s2_time)