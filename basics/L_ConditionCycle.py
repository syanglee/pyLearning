# Conditional judgment
# python3中，input函数统一返回字符串，因此需要用int()函数转置一下整数类型
age = int(input('please input your age: '))
if age >= 18:
    print("your age is ", age)
    print("You are adult.")
elif age >= 6:
    print("You are teenager.")
else:
    print("You are kid.")

# Cycle
names = ["Michael", "Bob", "Terry"]
for name in names:
    print(name)

# 计算1到100的整数之和，使用for循环
sum = 0
# range(n)函数可以生成一个整数序列，序列是从0开始小于n的整数
for x in list(range(101)):
    sum = sum + x
print(sum)

#计算1到100的整数之和，使用while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)