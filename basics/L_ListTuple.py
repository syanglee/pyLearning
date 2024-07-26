# list  列表
classmates = ["Michael", "Bob", "Terry"]

# 变量classmates就是一个list。用len()函数可以获得list元素的个数
print(classmates)
print(len(classmates))

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[0])

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-1])
# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, "Jack")
print(classmates)

# 要删除list末尾的元素，用pop()方法
classmates.pop()
print(classmates)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print(classmates)

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = "Sarah"
print(classmates)

# list元素可以是不同数据类型的，也可以包含另一个list
L = ['Apple', [1, 3, 5, 7, 9], 123, True]
print(len(L))
print(len(L[1]))

# list排序
lsort = ['c', 'b', 'a']
lsort.sort()
print(lsort)

# tuple 元组，tuple不能变，它没有append()，insert()这样的方法
mates = ('Michael', 'Bob', 'Tracy')
print(mates)
print(mates[0])

# 可变的tuple
t = ("a", "b", ["c", "d"])
t[2][0] = "X"
t[2][1] = "Y"
print(t)

# 练习
L = [['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa']]

print(L[0][0])
# 输出 Apple
print(L[1][1])
# 输出 Python
print(L[2][2])
# 输出 Lisa

# Tuple 元组
# 当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
# 定义一个空的tuple，可以写成()
t = ()

a=(1,True,0,'Apple',[1,2,[1,3]])
print(type(a))
# 输出 <class 'tuple'>
# 通过索引访问
print(a[2])
# 输出 0

print(a[-1])
# 输出 [1,2,[1,3]]

# 通过切片访问
print(a[0:3])
# 输出 （1, True, 0）

print(a[:-1])
# 输出 (1, True, 0, 'Apple')

# 通过 +、* 添加元素
a=(1,2,3)
a+=(4,5,6)
print(a)
# 输出 (1,2,3,4,5,6)

b=a*3
print(b)
# 输出 (1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)

# 同样适用于元组的一些内置函数
a=(1,3,5)

# 判断一个元素是否存在于元组中
print(1 in a)
# 输出 True

# 获取元组的长度
print(len(a))
# 输出 3

# 获取元组中最大元素
print(max(a))
# 输出 5

# 获取元组中最小元素
print(min(a))
# 输出 1

# 获取元组中元素的下标
print(a.index(3))
# 输出 1

# 获取元组中元素3的个数
print(a.count(3))
# 输出 1

# 计算元组中元素的和
print(sum(a))
# 输出 9

# 元组Turple与列表List的区别
# 1.元组的不可变性
# a=(1,2,3,4,5)
# a[0] = 10 是会报错的

# 删除元组，只能使用del清空元组
a=(1,2,3,4)
del a

# 元组的一些坑
# 定义一个元素的列表
print(type([1]))
# 输出 <class 'list'>

# 定义一个元素的元组，
print(type((1)))    # 这是一个tuple的陷阱：括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
# 输出 <class 'int'>
# 上面的(1)在python中是数学运算符号，因此输出的是int类型

# 正确的做法是在元素后面添加一个逗号
print(type((1,)))
# 输出<class 'tuple'>

# 元组中的元素不能修改，但元组中元素里面的元素可以修改，如下面的代码
a=(1,2,[3,4,5])
a[-1][-1]=10   # 这里修改的不是元组中的元素，而是[3,4,5]这个列表中的元素
print(a)
# 输出 (1,2,[3,4,10])
a[2].append(6)
print(a)
# 输出 (1, 2, 10, 6)

