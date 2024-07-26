from typing import Union, TypeVar

"""
Union 联合类型

"""

# 普通变量设置 Union 联合类型注解
var_1: Union[int, str] = 0
var_2: Union[int, str] = "0"
var_3: Union[int, str] = None

# 容器变量设置 Union 联合类型注解
var_list: [Union[int, str]] = [1, "Tom", 2, "Jerry"]
var_dict: [Union[int, str], Union[int, str]] = {"Name": "Tom", "age": 18}

# print_value()函数接受一个Union类型的参数 value, value 可以是int、float或str类型中的任何一个
def print_value(value: Union[int, float, str]):
    print(value)

print_value(1)
print_value(1.0)
print_value("1")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
class Animal:
    def __init__(self, spices: str):
        self.spices = spices

T = TypeVar('T', Person, Animal)

def print_info(obj: Union[T, int]):
    if isinstance(obj, int):
        print(f"Object: {obj.__class__}")
        print("Value = {obj}")
    else:
        print(f"Object: {obj.__class__}")
        print("Oject info: ",obj.__dict__)

p = Person("Alice", 20)
a = Animal("Tiger")

print_info(10)
print_info(p)
print("Person name = ", p.get_name())
print("Person age = ", p.get_age())
print_info(a)