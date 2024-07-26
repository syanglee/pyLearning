import torch

# 查看GPU的设备数量
print("查看GPU的设备数量：")
print(torch.cuda.device_count())

# 使用Cuda之前都需要检测一下cuda是否可用，没检测就默认没有
print("检测cuda是否可用：")
print(torch.cuda.is_available())


# 创建一个tensor，类型为float32，大小为3x3，并使用现有数据初始化:
t = torch.tensor([[1, 2, 3,2,1], [4, 5, 6,6,6],[7,8,9,0,1]],dtype=torch.float32)

# 输出tensor的大小
print("输出tensor的大小：")
print(t.size())

# 张量的形状包含了关于张量的轴、秩、索引信息；
# 输出张量的形状（shape）或称为张量的秩；张量的秩表示了张量中存在的维数（即张量的轴的数目）；
# 在pytorch中张量的size()和张量的形状是一样的。即张量轴的数目 = shape的长度
print("输出张量的秩：")
print(t.shape)

# 输出tensor的0轴的数目
print("输出tensor的第1个轴的数目：")
print(t.size(0))
# 输出tensor的1轴的数目
print("输出tensor的第2个轴的数目：")
print(t.size(1))

# 输出tensor的秩（shape）的长度，即维数
print("输出维数：")
print(len(t.shape))

# 输出tensor的形状的乘积，prod() 将数组tensor中的元素相乘
print("输出tensor的形状的乘积：")
print(torch.tensor(t.shape).prod())

# 输出tensor的元素个数
print("输出tensor的元素个数：")
print(t.numel())

# 创建一个 5x3 矩阵, 但是未初始化
x = torch.empty(5, 3)
print("输出一个未初始化的5x3矩阵：")
print(x)

# 创建一个0填充的矩阵，数据类型为long
x = torch.zeros(5, 3, dtype=torch.long)
print("输出一个5x3的值为0的矩阵：")
print(x)

# 覆盖 dtype! 对象的size 是相同的，只是值和类型发生了变化
x = torch.randn_like(x, dtype=torch.float) 
print("输出一个5x3的值为随机数矩阵：")
print(x)

# new_* 方法来创建对象
x = x.new_ones(5, 3, dtype=torch.double)
print("输出一个5x3的值为1的矩阵x：")
print(x)

# 创建一个随机初始化的矩阵
y = torch.rand(5, 3)
print("初始化一个5x3的值为随机数的矩阵y：")
print(y)

# 加法1：
print("方法1：矩阵x + 矩阵y = ")
print(x+y)

# 加法2：
print("方法2：矩阵x + 矩阵y = ")
print(torch.add(x,y))

# 加法3：提供输出tensor作为参数
result = torch.empty(5, 3)
torch.add(x, y, out=result) 
print("方法3：矩阵x + 矩阵y = ")
print(result)

# 加法4：adds x to y；任何 以``_`` 结尾的操作都会用结果替换原变量. 例如: ``x.copy_(y)``, ``x.t_()``, 都会改变 ``x``.
y.add_(x)
print("方法4：矩阵x + 矩阵y = ")
print(y)

# 使用与NumPy索引方式相同的操作来进行对张量的操作
# 对y切片，取第二列元素，与 print(y[...,1]) 相同
print("对y切片，取第二列元素：")
print(y[:,1])

# 对y切片，取第二行元素，与 print(y[1,...]) 相同
print("对y切片，取第二行元素：")
print(y[1,:])

# 对y切片，取第二列的2至4行
print("对y切片，取第二列的2至4行：")
print(y[1:4,1])
# 对y切片，取第2至3行的全部元素，与 print(y[1:3,...]) 相同
print("对y切片，取第2至3行的全部元素：")
print(y[1:3,:])

w = torch.rand(3, 5)
print("矩阵w = ")
print(w)
print("矩阵t = ")
print(t)
# 矩阵乘法
print("矩阵w × 矩阵t = ")
print(torch.multiply(w,t))

# torch.view 与Numpy的reshape类似
z = torch.tensor([[1, 2], [3, 4]])
print("矩阵z = ")
print(z)

# 将张量转换为2行4列的形状
x_view1 = z.view(2,4)
# 将张量转换为一行一列的形状（注意：-1表示自动计算行数）
x_view2 = z.view(-1,1)
# 将张量转换为一行一列的形状（注意：-1表示自动计算列数）
x_view3 = z.view(1, -1) 
# 打印转换后的张量
print("\nView 1:")
print(x_view1)
print("\nView 2:")
# print(x_view2)
print("\nView 3:")
print(x_view3)




