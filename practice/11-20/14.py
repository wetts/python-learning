'''
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

def reduceNum(n):
    print(n, end=' = ')

    if not isinstance(n, int) or n <= 0:
        print('请输入一个正确的数字 !')
        exit(0)
    elif n in [1]:
        print(n)

    while True:
        tmp = int(sqrt(n)) + 1
        tmpInt = 0
        flag = True
        for i in range(2, tmp):
            if n % i == 0:
                flag = False
                tmpInt = i
                n //= i
                break
        if flag:
            print(n)
            break
        else:
            print(i, end=' * ')

reduceNum(90)

reduceNum(100)
