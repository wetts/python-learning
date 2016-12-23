'''
有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数　
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(input('the total number is:\n'))
    m = int(input('back m:\n'))

    def move(array, n, m):
        return array[m:n] + array[0:m]

    number = []
    for i in range(n):
        number.append(int(input('input a number:\n')))
    print('orignal number:', number)

    print('after moved:', move(number, n, m))
