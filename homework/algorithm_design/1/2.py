# -*- encoding: utf-8 -*-
'''
@File    :   2.py
@Time    :   2019/10/11 19:52:34
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   分别用递归法和非递归法求Fibonacci数列的前1000位，并比较计算时间的差异.
'''
# here put the import lib
import time
import sys
sys.setrecursionlimit(100000)


def fibonacci(n: int):
    arr = []
    a, b = 1, 1

    arr.append(a)
    if n == 1:
        return arr
    arr.append(b)
    if n == 2:
        return arr

    for _ in range(n - 2):
        a, b = b, a + b
        arr.append(b)

    return arr


def fibonacci_recursive(n: int, a: int = 1, b: int = 1):
    arr = []
    if n >= 1 and a == 1 and b == 1:
        arr.append(a)
        n -= 1
    if n >= 1 and a == 1 and b == 1:
        arr.append(b)
        n -= 1

    if n >= 1:
        arr.append(a + b)
        n -= 1
        arr = arr + fibonacci_recursive(n, b, a + b)

    return arr


if __name__ == '__main__':
    n = 1000
    start = time.time()
    a1 = fibonacci(n)
    print('非递归法生成Fibonacci数列前 %d 项，花费 %f 秒' % (n, time.time() - start))
    start = time.time()
    a2 = fibonacci_recursive(n)
    print('递归法生成Fibonacci数列前 %d 项，花费 %f 秒' % (n, time.time() - start))
