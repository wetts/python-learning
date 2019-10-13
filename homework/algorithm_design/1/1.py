# -*- encoding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2019/10/11 19:51:21
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   输入一个自然数(<90000),  分别用递归法和非递归法求其二机制表示.
'''
# here put the import lib
import random


def to_binary_recursive(n: int):
    if n <= 1:
        return str(n)
    return to_binary_recursive(n // 2) + str(n % 2)


def to_binary(n: int):
    result = ''
    while True:
        result = str(n % 2) + result
        if n <= 1:
            break
        n = n // 2
    return result


if __name__ == '__main__':
    n = random.randint(0, 90000)
    print('n 的二进制（递归算法）为 %s' % to_binary_recursive(n))
    print('n 的二进制（非递归算法）为 %s' % to_binary(n))
