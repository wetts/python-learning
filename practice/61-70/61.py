'''
打印出杨辉三角形（要求打印出10行）。　　
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def fun(n):
    return fun1(0, n, [])

def fun1(current, max, arr):
    if current == 0:
        arr.append([1])
    else:
        a = []
        for i in range(current + 1):
            if i == 0 or i == current:
                a.append(1)
            else:
                a.append(arr[current - 1][i] + arr[current - 1][i - 1])
        arr.append(a)
    if current == max - 1:
        return arr
    else:
        return fun1(current + 1, max, arr)

print(fun(10))
