# -*- encoding: utf-8 -*-
'''
@File    :   2.py
@Time    :   2019/12/02 14:17:31
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   利用动态规划算法求最长公共子序列
'''

# here put the import lib


def bottom_up_dp_lcs(str_a, str_b):
    """
    longest common subsequence of str_a and str_b
    """
    if len(str_a) == 0 or len(str_b) == 0:
        return 0
    dp = [[0 for _ in range(len(str_b) + 1)] for _ in range(len(str_a) + 1)]
    for i in range(1, len(str_a) + 1):
        for j in range(1, len(str_b) + 1):
            if str_a[i-1] == str_b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max([dp[i-1][j], dp[i][j-1]])
    print("length of LCS is :", dp[len(str_a)][len(str_b)])
    # 输出最长公共子序列
    i, j = len(str_a), len(str_b)
    LCS = ""
    while i > 0 and j > 0:
        if str_a[i-1] == str_b[j-1] and dp[i][j] == dp[i-1][j-1] + 1:
            LCS = str_a[i - 1] + LCS
            i, j = i-1, j-1
            continue
        if dp[i][j] == dp[i-1][j]:
            i, j = i-1, j
            continue
        if dp[i][j] == dp[i][j-1]:
            i, j = i, j-1
            continue
    print("LCS is :", LCS)


if __name__ == "__main__":
    bottom_up_dp_lcs('abdfg', 'abcdfg')
