# -*- coding: utf-8 -*-

import random

print(random.random())  # 用于生成一个0到1的（0<=n<1.0）
print(random.uniform(1, 10))  # 用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。（a<=n<= b）
print(random.randint(1, 10))  # 用于生成一个指定范围内的整数。（a<=n<= b）
print(random.randrange(10, 30, 2))  # 从指定范围内，按指定基数递增的集合中获取一个随机数。

lst = ['python', 'C', 'C++', 'javascript']
str1 = ('I love python')
print(random.choice(lst))  # random.choice从序列中获取一个随机元素。
print(random.choice(str1))

random.shuffle(lst)  # 用于将一个列表中的元素打乱,即将列表内的元素随机排列。
print(lst)
s_l = list(str1)
random.shuffle(s_l)
print(s_l)

print(random.sample(lst, 2))  # 从指定序列中随机获取指定长度的片断并随机排列。注意：sample函数不会修改原有序列。
print(lst)