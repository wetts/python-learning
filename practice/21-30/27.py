'''
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def output(s, l):
    if l==0:
       return
    print(s[l - 1], end='')
    output(s, l - 1)

str = 'abcd'
output(str,len(str))
