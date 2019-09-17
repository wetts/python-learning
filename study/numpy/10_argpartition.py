# -*- coding: utf-8 -*-

import numpy as np

x = np.random.randint(1, 100, 10)
print(x)
i = np.argpartition(x, 3)
print(i)
print(x[i])
print(np.partition(x, 3))
