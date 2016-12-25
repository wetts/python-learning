'''
Python内置的sorted()函数就可以对list进行排序
'''

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

print(sorted([36, 5, -12, 9, -21]))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# 忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写）
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))