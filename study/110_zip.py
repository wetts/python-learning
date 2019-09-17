# -*- coding: utf-8 -*-

a = range(10)
b = range(100, 110)

tuple1 = zip(a)
print(type(tuple1))
print(tuple1)
print(list(tuple1))

print(list(zip(a, b)))


# zip()函数有2个参数
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
p = [[2, 2, 2],  [3, 3, 3]]
# 行与列相同
print("行与列相同:\n", list(zip(m, n)))
# 行与列不同
print("行与列不同:\n", list(zip(m, p)))

print("".center(50, "-"))
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]] 
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
print("*zip(m, n)返回:\n", *zip(m, n))
m2, n2 = zip(*zip(m, n))
# 若相等，返回True；说明*zip为zip的逆过程
print(m == list(m2) and n == list(n2))
