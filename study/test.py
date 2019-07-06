# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def add(n,i):
    return n+i

g = (i for i in range(4))

for n in [1,10]:
    print(n)
    g = (add(n,i) for i in g)
    print(g)

print(list(g))