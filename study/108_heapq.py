# -*- coding: utf-8 -*-

import heapq
import random

arr = []
for i in range(10):
    heapq.heappush(arr, (random.uniform(1, 10), random.randint(1, 5)))

print(arr)
print([heapq.heappop(arr) for i in range(len(arr))])


arr2 = []
heapq.heappush(arr2, (2, 5))
heapq.heappush(arr2, (2, 4))
heapq.heappush(arr2, (2, 5))
print([heapq.heappop(arr2) for i in range(len(arr2))])
print((2, 4) > (2, 5))