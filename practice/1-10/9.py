'''
暂停一秒输出。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

myD = {1: 'a', 2: 'b'}

for key, value in dict.items(myD):
	print(key, value)
	time.sleep(1) # 暂停 1 秒

print('--------------------------')

for key in myD.keys():
	print(key, myD[key])
	time.sleep(1) # 暂停 1 秒
