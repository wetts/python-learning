'''
时间函数举例1。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import time
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))
