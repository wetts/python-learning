# -*- coding: utf-8 -*-

# 实例的__dict__仅存储与该实例相关的实例属性
# 类的__dict__存储所有实例共享的变量和函数(类属性，方法等)，类的__dict__并不包含其父类的属性
# dir()是Python提供的一个API函数，dir()函数会自动寻找一个对象的所有属性(包括从父类中继承的属性)。

# 并不是所有对象都拥有__dict__属性。许多内建类型就没有__dict__属性，如list，此时就需要用dir()来列出对象的所有属性。
class A():
    s = "this is A (str)"
    __s = "this is A (__str)"
    class_super_s = __s = "this is A (class_super_str)"

    def __init__(self):
        self._s = "this is A (_s)"
        self.super_s = "this is A (super_s)"
    
    # 成员方法
    # 需要传入参数，默认名称为 self，用其他名称也可以
    def print_str(self):
        print(self.s, self.__s)

    # 类方法
    # 第一个参数需要是表示自身类的 cls 参数
    @classmethod 
    def class_method(cls):
        print(cls.__s, "this is A class method")

    # 静态方法不需要 cls 参数
    @staticmethod
    def static_method():
        print("this is A static method")

class B(A):
    s = "this is B"
    __s = "this is B (__str)"

    def __init__(self):
        self._s = "this is B (_s)"

if __name__ == '__main__':
    a = A()
    a.print_str()
    A.static_method()
    A.class_method()

    b = B()
    b.print_str()
    B.static_method()
    B.class_method()

    print("\n", "dir(a)", "\n")
    print(dir(a))
    print("\n", "a.__dict__", "\n")
    print(a.__dict__)
    print("\n", "dir(A)", "\n")
    print(dir(A))
    print("\n", "A.__dict__", "\n")
    print(A.__dict__)
    print("\n", "dir(b)", "\n")
    print(dir(b))
    print("\n", "b.__dict__", "\n")
    print(b.__dict__)
    print("\n", "dir(B)", "\n")
    print(dir(B))
    print("\n", "B.__dict__", "\n")
    print(B.__dict__)