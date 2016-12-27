'''
字符串日期转换为易读的日期格式。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from dateutil import parser
dt = parser.parse("Aug 28 2015 12:00AM")
print(dt)
