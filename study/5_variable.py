# 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
# -*- coding: utf-8 -*-

# 赋值方式
a,b,c=[1,2,3]

a,b,c=(1,2,3)

a,b,c=1,2,3

# 用r''表示''内部的字符串默认不转义
print(r'\\\t\\')

# 多行
print('''line1
line2''')

print(1.2e-5)
print(1.23e9)

print(True)
print(3 > 2)

print(True and False or False)
print(not True)

print(None)

print("10 / 3 = %s" % (10 / 3))

print("10 // 3 = %s" % (10 // 3))

print("10 %% 3 = %s" % (10 % 3))

a = 'abc'
b = a.replace('a', 'A')
print(b)
