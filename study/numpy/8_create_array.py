# -*- coding: utf-8 -*-

import numpy as np


# Input
arr = np.arange(9).reshape(3, 3)

# Solution Method 1:
rand_arr = np.random.randint(
    low=5, high=10, size=(5, 3)) + np.random.random((5, 3))
print(rand_arr)

# Solution Method 2:
rand_arr = np.random.uniform(5, 10, size=(5, 3))
np.set_printoptions(precision=3)
print(rand_arr)


print("".center(50, "-"))
np.random.seed(100)
rand_arr = np.random.random([3, 3])/1e3
np.set_printoptions(suppress=False)
print(rand_arr)


print("".center(50, "-"))
np.set_printoptions(threshold=6)
a = np.arange(15)
print(a)
