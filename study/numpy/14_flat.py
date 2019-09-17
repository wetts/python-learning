# -*- coding: utf-8 -*-

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.flat)
print(np.array(a.flat))
print(a[:, 2])
print(np.array(a[:, 2].flat))
print(a.size)