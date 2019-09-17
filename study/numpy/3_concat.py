# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# Answers
# Method 1:
print(np.concatenate([a, b], axis=0))
print(np.concatenate([a, b], axis=1))

# Method 2:
print(np.hstack([a, b]))
print(np.vstack([a, b]))

# Method 3:
print(np.c_[a, b])
print(np.r_[a, b])
# > array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
# >        [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])


print("".center(50, "-"))
c = np.arange(10).reshape((1, -1))
print(c)
print(np.append(c, np.arange(10, 20).reshape(1, -1), axis=1))

print("".center(50, "-"))
d = np.array([])
d = np.vstack((d, [1, 2, 3, 4]))
print(d)
d = np.append(d, [[1, 2, 3, 4]], axis=0)
print(d)
