'''
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

arr = [1, 5, 8, 3, 5, 7, 2, 8, 9, 0, 2, 4]
arr.sort()

num = int(input('input num:\n'))

def insert(arr, num):
    if num >= arr[len(arr) - 1]:
        arr.append(num)
    elif num <= arr[0]:
        arr.insert(0, num)
    else:
        start, end = 0, len(arr) - 1
        while start <= end:
            tmp = (start + end) // 2
            if arr[tmp] > num:
                end = tmp - 1
            elif arr[tmp] < num:
                start = tmp + 1
            else:
                arr.insert(tmp, num)
                break
    return arr

print(insert(arr, num))
