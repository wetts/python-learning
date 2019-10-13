# -*- encoding: utf-8 -*-
'''
@File    :   5.py
@Time    :   2019/10/13 20:25:24
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   在8×8格的国际象棋上摆放八个皇后，使其不能互相攻击，即任意两个皇后都不能处于同一行、同一列或同一斜线上，输出所有摆法。
'''

# here put the import lib


def queens(num: int = 8,  result: list = [], tmp: list = []):
    for i in range(num):
        if not conflict(i, tmp):
            if len(tmp) < num - 1:
                queens(num, result, tmp + [i])
            else:
                result.append(tmp + [i])
                return

    return result


def conflict(pos: int, tmp: list):
    row_num = len(tmp)
    for i, v in enumerate(tmp):
        if abs(pos - v) in (0, row_num - i):
            return True
    return False


if __name__ == "__main__":
    l = queens()
    print(l)
    print(len(l))
