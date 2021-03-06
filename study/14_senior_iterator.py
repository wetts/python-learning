# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
我们已经知道，可以直接作用于for循环的数据类型有以下几种：
    一类是集合数据类型，如list、tuple、dict、set、str等；
    一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象
'''
from collections import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 可以使用isinstance()判断一个对象是否是Iterator对象
from collections import Iterator

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('abc'), Iterator))
