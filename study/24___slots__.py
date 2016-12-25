'''
Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
'''
#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
class Student(object):
    __slots__ = ('name', 'age', 'set_age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
# s.score = 99
print(s.name)

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) # 测试结果

s2 = Student() # 创建新的实例
# s2.set_age(25)

class Student2(Student):
    pass

ss = Student2()
ss.score = 99 # 绑定属性'score'
print(ss.score)

class Student3(Student):
    __slots__ = ('a') # 用tuple定义允许绑定的属性名称

sss = Student3()
sss.age = 1
sss.score = 99
print(sss.score)