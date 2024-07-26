# List generation
l = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in l])

"""
range(start, stop[, step]) 
创建一个整数列表
    start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
    stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
    step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
注意：Python3 range() 返回的是一个可迭代对象（类型是对象），而不是列表类型，所以打印的时候不会打印列表
"""
for r in range(1,10):
    print("Print range(1,51) = ", r)