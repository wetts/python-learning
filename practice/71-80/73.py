'''
反向输出一个链表。

列表的reverse方法是对列表本身进行修改，它的返回值为空

[::-1]是返回一个反向的
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('please input a number:\n'))
        ptr.append(num)
    print(ptr)
    ptr.reverse()
    print(ptr)
