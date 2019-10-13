# -*- encoding: utf-8 -*-
'''
@File    :   slice.py
@Time    :   2019/10/13 13:38:38
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   切片
'''

# here put the import lib


if __name__ == "__main__":
    #%%
    a = [1, 2, 3, 4, 5, 6]
    b = a
    c = a[::2]
    d = a[:]
    print(id(a), a)
    print(id(b), b)
    print(id(c), c)
    print(id(d), d)
    print(id(c[0]), c)
    print(id(c[1]), c)

    print(''.center(50, '-'))
    a[::2] = [0] * 3
    print(a)
    
    print(''.center(50, '-'))
    b[1::2] = [1] * 3
    print(a)
    print(b)
