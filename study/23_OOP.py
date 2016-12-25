'''
面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
class Student(object):

    '''
    注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身

    有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去

    如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
    '''
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    # 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
print(bart._Student__name)

print(bart.get_name())
bart.__name = 'New Name'
# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量
print(bart.__name)
print(bart.get_name())

###################################
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    pass

dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = list() # a是list类型

print(isinstance(a, list))
print(isinstance(cat, Animal))
print(isinstance(cat, Dog))

def run_twice(a):
    a.run()

run_twice(Animal())
run_twice(Dog())

#############################
### 判断对象类型，使用type()函数
print(type(cat))
import types
print(type(lambda x: x) == types.LambdaType)

### 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
print(isinstance(cat, Animal))
# 能用type()判断的基本类型也可以用isinstance()判断
print(isinstance(123, int))
# 可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
print(isinstance([1, 2, 3], (list, tuple)))

### 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print(dir('ABC'))
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的
print(len('ABC'))
print('ABC'.__len__())
# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x')) # 有属性'x'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(obj.y) # 获取属性'y'
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404
# 也可以获得对象的方法
fn = getattr(obj, 'power')
print(fn())