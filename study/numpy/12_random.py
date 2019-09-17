# -*- coding: utf-8 -*-

import numpy as np

print(np.random.random(10))
print(np.random.randint(1, 11, 5))

x = np.random.randint(1, 11, 50)
print(np.random.choice(x, size=2))
