# -*- encoding: utf-8 -*-
'''
@File    :   4.py
@Time    :   2019/10/13 19:34:04
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   一个射击运动员打靶，靶一共有10环，连开6枪打中45环的可能性有多少种? （每一枪最少是0环，最多是10环）
'''

# here put the import lib


def execute(shoot_num: int, point_sum: int, bottom: int = 0, top: int = 10, result: list = [], tmp: list = []):
    if shoot_num * top < point_sum:
        return result

    if shoot_num == 1:
        if point_sum < top and point_sum > bottom:
            result.append(tmp + [point_sum])
        return result

    for i in range(bottom, top + 1):
        execute(shoot_num - 1, point_sum - i, bottom, i, result, tmp + [i])

    return result


if __name__ == "__main__":
    r = execute(6, 45)
    print('所有打靶环数的可能为：%s' % r)
    print('有 %d 种可能性' % len(r))
