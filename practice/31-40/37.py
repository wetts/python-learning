'''
对10个数进行排序。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    l = [9,1,2,7,6,8,3,4,0]
    print(l)

    # sort ten num
    for i in range(len(l)):
        min = i
        for j in range(i + 1,len(l)):
            if l[min] > l[j]:
                min = j
        l[i], l[min] = l[min], l[i]
    print('after sorted')
    print(l)
