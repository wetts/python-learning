# -*- coding: utf-8 -*-

import numpy as np

np.random.seed(100)
arr = np.random.randint(1, 11, size=(6, 10))
print(arr)
print(np.unique(arr, return_index=True, return_counts=True))


print(type({i for i in range(8)}))