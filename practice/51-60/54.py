'''
取一个整数a从右端开始的4〜7位。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = int(input('input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    # 8进制
    print('%o\t%o' % (a, d))
