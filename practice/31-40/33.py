'''
按逗号分隔列表。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

a = ['one', 'two', 'three']
print(','.join(str(i) for i in a))
