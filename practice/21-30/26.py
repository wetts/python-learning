'''
利用递归方法求5!。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def fun(n):
    if n == 0:
        return 1
    else:
        return fun(n - 1) * n

print(fun(5))
