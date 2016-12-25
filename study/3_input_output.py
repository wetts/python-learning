# -*- coding: utf-8 -*-

name = input('please enter your name: ')
print('hello', name)

# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数
a = input('please input number:')
print(10 / int(a))