# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# *后面的两个参数必需使用关键字参数传入,并且必填
def fun1(a, *, b, c):
    print(a, b, c)


fun1(2, b="aa", c=123)

print("####################")


# 如果关键字参数有默认值,就不是必填
def fun2(a, *, b, c=3):
    print(a, b, c)


fun2(2, b="aa")

print("####################")


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def fun3(*a, b, c):
    print(a, b, c)


fun3(1, 3, 5, 'aa', b="213", c="f")
