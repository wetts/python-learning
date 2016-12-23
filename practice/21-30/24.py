'''
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce

def fun(n):
    a, b = 2, 1
    for i in range(n):
        yield a / b
        a, b = a + b, a

print(reduce(lambda a, b : a + b, fun(20)))
print(sum(fun(20)))
