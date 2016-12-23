'''
输出9*9乘法口诀表。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %2d' % (i, j, i * j), end=' ')
    print('\n')
