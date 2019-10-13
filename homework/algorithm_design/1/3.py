# -*- encoding: utf-8 -*-
'''
@File    :   3.py
@Time    :   2019/10/12 21:57:03
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   用递归算法完成如下问题：有52张牌，使它们全部正面朝上，第一轮是从第2张开始，凡是2的倍数位置上的牌翻成正面朝下；第二轮从第3张牌开始，凡是3的倍数位置上的牌，正面朝上的翻成正面朝下,正面朝下的翻成正面朝上；第三轮从第4张牌开始，凡是4的倍数位置上的牌按上面相同规则翻转，以此类推，直到第一张要翻的牌超过52为止。统计最后有几张牌正面朝上，以及它们的位置号.
'''
# here put the import lib
import numpy as np


def execute(end: int, start: int = 2, arr: np.ndarray = None):
    if arr is None:
        arr = np.full(end, True)

    arr[start - 1: end: start] = ~arr[start - 1: end: start]

    if start < end:
        execute(end, start + 1, arr)

    return arr


if __name__ == "__main__":
    arr = execute(52)
    result = np.where(arr == True)[0] + 1
    print('正面朝上的牌有 %d 张' % result.size)
    print('正面朝上的牌的位置号为（第一张牌位置是1）：%s' % result)
