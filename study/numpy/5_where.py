# -*- coding: utf-8 -*-

import numpy as np

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

print(np.where(a == b))


# Method 1
index = np.where((a >= 5) & (a <= 10))
print(a[index])

# Method 2:
index = np.where(np.logical_and(a >= 5, a <= 10))
print(a[index])
# > (array([6, 9, 10]),)

# Method 3: (thanks loganzk!)
print(a[(a >= 5) & (a <= 10)])
print((a >= 5) & (a <= 10))
print(a[[False, True, False, True, False, True, False, True, False, True]])
