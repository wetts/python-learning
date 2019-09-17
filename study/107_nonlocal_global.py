# -*- coding: utf-8 -*-

g = 'aabbcc'


def func1():
    print(locals())
    print(globals())
    global g
    g = 11
    print(g)
    print(locals())
    print(globals())


def func2():
    nl = 'local'

    def func3():
        nl = 3
        print(nl)

    def func4():
        nonlocal nl
        nl = 5
        print(nl)

    print(nl)
    func3()
    print(nl)
    func4()
    print(nl)


print(locals())
print(''.center(50, '-'))
func1()
print(''.center(50, '-'))
print(locals())
print(''.center(50, '-'))
func2()
