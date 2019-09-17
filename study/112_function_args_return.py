# -*- coding: utf-8 -*-


def f1():
    return 1, 2


def f2(a, b):
    return a + b

a, b = f1()
print(f2(a, b))
