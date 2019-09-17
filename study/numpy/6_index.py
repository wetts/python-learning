# -*- coding: utf-8 -*-

import numpy as np


x = np.array([[1,  2],  [3,  4],  [5,  6]])
print(x[[0, 1, 2],  0])
print(x[[0, 1, 2],  [0]])
print(x[[0, 1, 2],  [0, 1, 0]])
print(x[1, 1])
print("".center(50, "-"))
y = x[:, 1]
print(y)
x[2, 1] = 10
print(y)
print(x)
y[0] = 77
print(x)
z = x[0, 0]
z = 99
print(x)
print("".center(50, "-"))
print(x[:, :1])
print(x[[1], [1]])
print(x[[1, 1]])
print(x[:, [1, 1]])
print("".center(50, "-"))
y = x[:, [1]]
print(y)
x[2, 1] = 10
print(y)


print("".center(50, "-"))
x = np.array([[0,  1,  2], [3,  4,  5], [6,  7,  8], [9,  10,  11]])
print('我们的数组是：')
print(x)
print('\n')
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = a[1:3, 1:3]
c = a[1:3, [1, 2]]
d = a[..., 1:]
print(b)
print(c)
print(d)


x = np.array([[0,  1,  2], [3,  4,  5], [6,  7,  8], [9,  10,  11]])
print('我们的数组是：')
print(x)
print('\n')
# 现在我们会打印出大于 5 的元素
print('大于 5 的元素是：')
print(x[x > 5])


a = np.array([np.nan,  1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])

print("".center(50, "-"))
x = np.arange(32).reshape((8, 4))
print(np.ix_([1, 5, 7, 2], [0, 3, 1, 2]))
print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
print(x[[[1], [5]], [0, 3]])

print("".center(50, "-"))
y = np.arange(35).reshape(5, 7)
b = y > 20
print(b[:, 5])
print(y[b[:, 5]])

print("".center(50, "-"))
x = np.arange(5)
print(x[:, np.newaxis])
print(x[np.newaxis, :])
print(x[:, np.newaxis] + x[np.newaxis, :])

print("".center(50, "-"))
x = np.arange(0, 50, 10)
print(x)
x[np.array([1, 1, 3, 1])] += 1
print(x)
