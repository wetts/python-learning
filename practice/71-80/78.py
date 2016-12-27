'''
找到年龄最大的人，并输出。请找出程序中有什么问题。
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    m = 'li'
    for key, value in person.items():
        if person[m] < value:
            m = key

    print('%s,%d' % (m,person[m]))
