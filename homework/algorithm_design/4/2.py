# -*- encoding: utf-8 -*-
'''
@File    :   2.py
@Time    :   2020/01/10 01:09:56
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   设计算法，求一个正整数n的整数划分表示。例如正整数6有如下11种不同的划分
'''

# here put the import lib


def execute(num, max, res=[]):
    if num == 0:
        print(res)
        return 1

    count = 0
    for i in range(max, 0, -1):
        new_num = num - i
        r = res.copy()
        r.append(i)
        count += execute(new_num, new_num if new_num < i else i, r)

    return count


if __name__ == "__main__":
    n = 6
    print('数字 %d 一共有 %d 种划分' % (n, execute(n, n)))

