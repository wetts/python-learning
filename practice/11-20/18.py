'''
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce

n = int(input('n = :\n'))
a = int(input('a = :\n'))

def fun(a, n):
    base = 0
    for i in range(n):
        result = a + base
        yield result
        base = result * 10

print(reduce(lambda x, y : x + y, fun(a, n)))
