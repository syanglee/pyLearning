from multiprocessing import Pool
import time
"""
[1] map(func, iterable[, chunksize])
map函数只支持一个可迭代参数，它的多个参数迭代版本是starmap()。它会保持阻塞直到获得结果。具体而言这个方法很耗内存，推荐使用imap()

[2] map_async(func, iterable[, chunksize[, callback[, error_callback]]])
map()返回的是一个列表，这个方法返回的是一个对象，方法的功能同上。

starmap(func, iterable[, chunksize])和 map() 类似;
不过 iterable 中的每一项会被解包再作为函数参数。比如可迭代对象 [(1,2), (3, 4)] 会转化为等价于 [func(1,2), func(3,4)] 的调用。

[3] imap(func, iterable[, chunksize])
imap()方法的lazy版本。
这个方法会将可迭代对象分割为许多块，然后提交给进程池。
可以将 chunksize 设置为一个正整数从而（近似）指定每个块的大小可以。它支持多参数
"""
def func1(x):
    time.sleep(0.3)
    return x**2

def func2(x,y):
    time.sleep(0.3)
    return (x+y,x*y)

def main():
    begin = time.time()
    with Pool(8) as p:
        result = p.imap(func2, [(2,i) for i in range(8)])
        p.close()
        p.join()
    during = time.time() - begin
    print("func_2 result = ",result)
    print(f"imap func2 during: {during}")

def main2():
    begin = time.time()
    with Pool(8) as p:
        result2 = p.imap(func1, range(8),chunksize=1)   # 经测试 chunksize 值越大，执行速度越慢；但文档中说chunksize越大，速度越大。
        p.close()
        p.join()
    during = time.time() - begin
    print("func_2 result = ",result2)
    print(f"imap chunksize=2 func1 during: {during}")

if __name__ == "__main__":
    main()
    main2()