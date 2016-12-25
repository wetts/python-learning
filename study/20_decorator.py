# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数对象有一个__name__属性，可以拿到函数的名字
def now():
    print('2015-3-25')

print(now.__name__)

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 把@log放到now()函数的定义处，相当于执行了语句: now = log(now)
@log
def now():
    print('2015-3-25')

now()

'''
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数

wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数
'''

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的: now = log('execute')(now)
@log('execute')
def now():
    print('2015-3-25')

print(now.__name__)

# 返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

print(now.__name__)

####################
# 编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call %s():' % func.__name__)
        f = func(*args, **kw)
        print('end call %s():' % func.__name__)
        return f
    return wrapper

@log
def now():
    print('2015-3-25')

now()

@log
def p():
    return 1

print(p())