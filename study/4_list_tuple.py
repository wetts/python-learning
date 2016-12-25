#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['aaa', 'bbb', 'ccc']
print(classmates)
# print(classmates[3])
print(classmates[-1])

# 用len()函数可以获得list元素的个数
print("list length :%d" % (len(classmates)))

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('ddd')

# 可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'eee')
print(classmates)

# 要删除list末尾的元素，用pop()方法
print("pop: %s" % classmates.pop())
print(classmates)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
print("pop: %s" % classmates.pop(1))
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'fff'
print(classmates)

# list里面的元素的数据类型也可以不同
l = ['Apple', 123, True]
print("l: %s" % l)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print("s: %s" % s)

# 随机生成
a = range(5)
print(a)
print(list(a))

print("#############################")
######################
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
t = (1, 2)
print(t)

e = ()
print(e)

# 要定义一个只有1个元素的tuple，如果你这么定义：
p = (1)
print(p)

# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
q = (1,)
print(q)

# “可变的”tuple
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)