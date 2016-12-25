# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

# 获取循环下表
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 判断对象是否是可迭代对象
from collections import Iterable

print(isinstance('abc', Iterable))

print(isinstance(123, Iterable))
