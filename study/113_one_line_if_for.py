# -*- coding: utf-8 -*-

a = [1, 2, 3, 4]
print([0 if i < 2 else 1 for i in a])
print([0 for i in a if i < 2])


b = [[1, 2, 3, 4], [4, 3, 2, 1]]
print([[0 if j < 2 else 1 for j in i] for i in b])
