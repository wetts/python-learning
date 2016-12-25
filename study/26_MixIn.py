'''
MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Bat(Mammal, Flyable):
    pass