# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

a = np.array([0, 1, 2, 3, 4])
b = np.array((0, 1, 2, 3, 4))
c = np.arange(5)
d = np.linspace(0, 2 * np.pi, 5)
print(a)
print(b)
print(c)
print(d)
print(c[1:3])

aa = np.array([[11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25],
               [26, 27, 28, 29, 30],
               [31, 32, 33, 34, 35]])
print(aa[0, 1:4])
print(aa[:, 1])
print(type(aa))
print(aa.dtype)
print(aa.size)
print(aa.shape)
# itemsize 属性是每个项占用的字节数。这个数组的数据类型是int 64，一个int 64中有64位，一个字节中有8位，除以64除以8，你就可以得到它占用了多少字节
print(aa.itemsize)
print(aa.ndim)
# nbytes 属性是数组中的所有数据消耗掉的字节数。你应该注意到，这并不计算数组的开销，因此数组占用的实际空间将稍微大一点。
print(aa.nbytes)

print(np.full((2, 3, 2), 5))
print(np.random.random((2, 2)))

bb = np.arange(25)
bb = bb.reshape((5, 5))
print(bb ** 2)
print(aa < bb)
print(aa.dot(bb))
print(np.where(aa >= 24))
print(np.where(aa >= 4, 3, 4))
print(aa[aa > 29])

print(aa.sum(axis = 0))
print(aa.sum(axis = 1))
print(aa.sum())
print(aa.min())
print(aa.max())
# cumsum() 返回一个累加的列表
print(aa.cumsum())

indices = [1, 3, -1]
print(a[indices])


# Boolean masking
a = np.linspace(0, 2 * np.pi, 50)
b = np.sin(a)
print(b)
plt.plot(a, b)
mask = b >= 0
print(mask)
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()
