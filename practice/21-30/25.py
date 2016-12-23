'''
求1+2!+3!+...+20!的和。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def fun(n):
    s = 1
    while s <= n:
        r = 1
        for i in range(1, s + 1):
            r *= i
        yield r
        s += 1
    return 'done'

print(sum(fun(20)))
