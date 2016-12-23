'''
求输入数字的平方，如果平方运算后小于 50 则退出。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def SQ(x):
    return x * x
print('如果输入的数字小于 50，程序将停止运行。')

again = True
while again:
    num = int(input('Please input number'))
    print('运算结果为 %d' % (SQ(num)))
    if num >= 50:
        again = True
    else:
        again = False
