'''
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def fun(num):
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - i - 1]:
            return False
    return True

print(fun('123454321'))
