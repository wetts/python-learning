'''
暂停一秒输出。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
