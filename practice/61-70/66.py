'''
输入3个数a,b,c，按大小顺序输出。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    arr = []
    n1 = int(input('n1 = :\n'))
    arr.append(n1)
    n2 = int(input('n2 = :\n'))
    arr.append(n2)
    n3 = int(input('n3 = :\n'))
    arr.append(n3)

    print(arr)
    print(arr.sort())
