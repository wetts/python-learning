'''
判断101-200之间有多少个素数，并输出所有素数。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

start = 2

for i in range(101, 200):
    end = int(sqrt(i)) + 1
    flag = True
    for j in range(start, end):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i, end=' ')
