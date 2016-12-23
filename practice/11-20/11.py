'''
古典问题：
有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def fun(max):
    a, b = 1, 1
    for i in range(max):
        yield a
        a, b = b, a + b
    return 'end'

for i in fun(10):
    print(i, end=' ')
