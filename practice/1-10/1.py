'''
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

list = []

list.append(input('请输入第一个数字'))
list.append(input('请输入第二个数字'))
list.append(input('请输入第三个数字'))
list.append(input('请输入第四个数字'))

print(list)

for i in list:
    for j in list:
        for k in list:
            if i != j and i != k and k != j:
                print(i, j, k)
