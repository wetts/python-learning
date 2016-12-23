'''
打印出菱形
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce

def fun(a):
    for i in range(a):
        printStart(a, i)
    for i in range(a - 1, -1, -1):
        printStart(a, i)

def printStart(a, i):
    blank = reduce(lambda x, y : x + y, (' ' for j in range(a - i)))
    star = reduce(lambda x, y : x + y, ('*' for j in range(i * 2 + 1)))
    print(blank + star + blank)

fun(4)
