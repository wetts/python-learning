'''
一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math

c = 0
i = 1

while True:
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print(i)
        c += 1
        if c == 3:
            break
    i += 1
