#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('ABC'.encode('ascii'))

print(b'ABC'.decode('ascii'))
print('xxx, %s' % b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))