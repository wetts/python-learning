'''
求100之内的素数。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

def fun(start, end):
    for i in range(start, end):
        tmp = int(sqrt(end)) + 1
        flag = True
        for j in range(2, tmp):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(i)
            
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
fun(lower, upper)
