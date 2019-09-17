# -*- coding: utf-8 -*-
# dict的key必须是不可变对象
# 因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

# !/usr/bin/env python3

# dict
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 如果key不存在，dict就会报错
# print(d['Thomas'])

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in d)
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))
print(d.get('Thomas', -1))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d.pop('Bob'))

dd = {'a': {'aa': 3, 'bb': {'aa': 5}}}
(k, v), = dd.items()
print(k, v)

print("#####################")
#####################
# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合
s = set([2, 1, 2, 3, 1])
print(s)

s.add(4)
print(s)

s.remove(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
