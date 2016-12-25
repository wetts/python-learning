# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 要生成[1x1, 2x2, 3x3, ..., 10x10]的list
print([x * x for x in range(1, 11)])

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])

# 还可以使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
