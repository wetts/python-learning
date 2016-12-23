'''
输入某年某月某日，判断这一天是这一年的第几天？
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

sum = months[month - 1]

if month > 2:
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        sum += 1

print(sum)
