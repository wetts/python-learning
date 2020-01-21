# -*- encoding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2020/01/09 21:52:53
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   动态规划法求0-1背包问题
'''

'''
动态规划核心：计算并存储小问题的最优解，并将这些最优解组合成大问题的最优解。

对于第 i 个物品，放入后可以取得最大的价值，那么，前 i-1 个物品在背包容量为 w-w[i] 的情况下能够取到最大的价值。
'''

# here put the import lib




import numpy as np
def execute(weight_list, value_list, max_weight):
    length = len(value_list)
    res_arr = np.zeros((length, max_weight), dtype=np.int32)

    for i in range(0, length):
        for j in range(0, max_weight):
            if weight_list[i] <= j:
                res_arr[i, j] = max(res_arr[i - 1, j - weight_list[i]] + value_list[i], res_arr[i-1, j])
            else:
                res_arr[i, j] = res_arr[i - 1, j]
    return res_arr[-1, -1], res_arr


if __name__ == '__main__':
    w = (92, 4, 43, 83, 84, 68, 92, 82, 6, 44, 32, 18, 56, 83, 25, 96, 70, 48, 14, 58)
    v = (44, 46, 90, 72, 91, 40, 75, 35, 8, 54, 78, 40, 77, 15, 61, 17, 75, 29, 75, 63)
    weight = 878
    result, res = execute(w, v, weight)
    print(res)
    print("根据动态规划算法得到的最优价值为：", result)
