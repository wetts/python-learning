'''
斐波那契数列。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def fib(max):
    a, b = 0, 1
    for i in range(max):
        yield b
        a, b = b, a + b
    return 'done'

for i in fib(6):
    print(i)
