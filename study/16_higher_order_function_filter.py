'''
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''

# ! /usr/bin/env python
# -*- coding: utf-8 -*-

# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

'''
求素数
计算素数的一个方法是埃氏筛法
首先，列出从2开始的所有自然数，构造一个序列；
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉；
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉；
取新序列的第一个数5，然后用5把序列的5的倍数筛掉；
不断筛下去，就可以得到所有的素数
'''
# 用Python来实现这个算法，可以先构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 然后定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 最后，定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

#########################
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数
def is_palindrome(n):
    i,u = n, 0
    while i != 0:
        u = i % 10 + u * 10
        i = i // 10
    return n == u

output = filter(is_palindrome, range(1, 1000))
print(list(output))

def is_palindrome(n):
    return n == int(str(n)[::-1])

output = filter(is_palindrome, range(1, 1000))
print(list(output))