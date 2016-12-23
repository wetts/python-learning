'''
学习使用按位与 & 。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = 77
    b = a & 3
    print('a & b = %d' % b)
    b &= 7
    print('a & b = %d' % b)

    print(0 & 0)
    print(0 & 1)
    print(1 & 0)
    print(1 & 1)
