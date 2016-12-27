'''
计算字符串中子串出现的次数。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    str1 = input('input a string:\n')
    str2 = input('input a sub string:\n')
    ncount = str1.count(str2)
    print(ncount)
