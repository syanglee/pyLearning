# Dict dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# dict的key必须是不可变对象，在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
names = {'Michael': 95, "Tracy": 85, "Bob": 75}
print(names['Michael'])

# 多次对一个key放入value，后面的值会把前面的值冲掉
names['Adam'] = 90
names['Adam'] = 88
print(names['Adam'])

if 'Joy' in names:
    print(names['Joy'])
else:
    print(names.get('Joy'))
    print(names.get('Joy', -1))

# dict有以下几个特点：
# 1)查找和插入的速度极快，不会随着key的增加而变慢；
# 2)需要占用大量的内存，内存浪费多。
# list相反：
# 1)查找和插入的时间随着元素的增加而增加；
# 2)占用空间小，浪费内存很少。

# Set 也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 1, 2, 2, 3, 3])
print(s)

# 通过add(key)方法添加元素到set中，可以重复添加，但不会有效果
s.add(4)
# 通过remove(key)方法可以删除元素
s.remove(1)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# 即使下面的结果s3可能是有序排列的，但set是无序的，无序的，无序的
l = [7, 1, 3, 5, 4, 2, 9, 6, 8]
s3 = set(l)
s3.add(0)
print(s3)

# set和dict的唯一区别仅在于没有存储对应的value。
# 但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

# 不可变对象
# str是不变对象
a = 'cba'
b = a.replace('a', 'A')
print(b)
# 而list是可变对象
c = ['c', 'b', 'a']
# 排序
c.sort()
print(c)
