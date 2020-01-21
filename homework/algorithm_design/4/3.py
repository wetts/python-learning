# -*- encoding: utf-8 -*-
'''
@File    :   3.py
@Time    :   2020/01/10 02:14:54
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   
'''

# here put the import lib
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
from numpy.matlib import rand
from matplotlib.artist import getp
import copy

# 初始三十个城市坐标
city_x = [41, 37, 54, 25, 7, 2, 68, 71, 54, 83, 64, 18, 22, 83, 91, 25, 24, 58, 71, 74, 87, 18, 13, 82, 62, 58, 45, 41, 44, 4]
city_y = [94, 84, 67, 62, 64, 99, 58, 44, 62, 69, 60, 54, 60, 46, 38, 38, 42, 69, 71, 78, 76, 40, 40, 7, 32, 35, 21, 26, 35, 50]
# 城市数量
n = 30
distance = [[0 for col in range(n)] for raw in range(n)]
# 初始温度 结束温度
T0 = 30
Tend = 1e-8
# 循环控制常数
L = 10
# 温度衰减系数
a = 0.98

# 构建初始参考距离矩阵


def get_distance():
    for i in range(n):
        for j in range(n):
            x = pow(city_x[i] - city_x[j], 2)
            y = pow(city_y[i] - city_y[j], 2)
            distance[i][j] = pow(x + y, 0.5)
    for i in range(n):
        for j in range(n):
            if distance[i][j] == 0:
                distance[i][j] = sys.maxsize

# 计算总距离


def cacl_best(rou):
    sumdis = 0.0
    for i in range(n-1):
        sumdis += distance[rou[i]][rou[i+1]]
    sumdis += distance[rou[n-1]][rou[0]]
    return sumdis

# 得到新解


def get_new_route(route, time):
    # 如果是偶数次，二变换法
    current = copy.copy(route)

    if time % 2 == 0:
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        temp = current[u]
        current[u] = current[v]
        current[v] = temp
    # 如果是奇数次，三变换法
    else:
        temp2 = random.sample(range(0, n), 3)
        temp2.sort()
        u = temp2[0]
        v = temp2[1]
        w = temp2[2]
        w1 = w + 1
        temp3 = [0 for col in range(v - u + 1)]
        j = 0
        for i in range(u, v + 1):
            temp3[j] = current[i]
            j += 1

        for i2 in range(v + 1, w + 1):
            current[i2 - (v-u+1)] = current[i2]
        w = w - (v-u+1)
        j = 0
        for i3 in range(w+1, w1):
            current[i3] = temp3[j]
            j += 1

    return current


def draw(best):
    result_x = [0 for col in range(n+1)]
    result_y = [0 for col in range(n+1)]

    for i in range(n):
        result_x[i] = city_x[best[i]]
        result_y[i] = city_y[best[i]]
    result_x[n] = result_x[0]
    result_y[n] = result_y[0]
    print(result_x)
    print(result_y)
    plt.xlim(0, 100)  # 限定横轴的范围
    plt.ylim(0, 100)  # 限定纵轴的范围
    plt.plot(result_x, result_y, marker='>', mec='r', mfc='w', label=u'Route')
    plt.legend()  # 让图例生效
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"x")  # X轴标签
    plt.ylabel(u"y")  # Y轴标签
    plt.title("TSP 问题结果")  # 标题

    plt.show()
    plt.close(0)


def solve():
    # 得到距离矩阵
    get_distance()
    # 得到初始解以及初始距离
    route = random.sample(range(0, n), n)
    total_dis = cacl_best(route)
    print("初始路线：", route)
    print("初始距离：", total_dis)
    # 新解
    newroute = []
    new_total_dis = 0.0
    best = route
    best_total_dis = total_dis
    t = T0

    while True:
        if t <= Tend:
            break
        # 令温度为初始温度
        for rt2 in range(L):
            newroute = get_new_route(route, rt2)
            new_total_dis = cacl_best(newroute)
            delt = new_total_dis - total_dis
            if delt <= 0:
                route = newroute
                total_dis = new_total_dis
                if best_total_dis > new_total_dis:
                    best = newroute
                    best_total_dis = new_total_dis
            elif delt > 0:
                p = math.exp(-delt / t)
                ranp = random.uniform(0, 1)
                if ranp < p:
                    route = newroute
                    total_dis = new_total_dis
        t = t * a
    print("现在温度为：", t)
    print("最佳路线：", best)
    print("最佳距离：", best_total_dis)
    draw(best)


if __name__ == "__main__":
    solve()
