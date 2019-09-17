# -*- coding: utf-8 -*-

from datetime import datetime
import requests
import PIL
from PIL import Image
from io import BytesIO
import numpy as np

# 从数组a中，替换所有大于30到30和小于10到10的值。
np.set_printoptions(precision=2)
np.random.seed(100)
a = np.random.uniform(1, 50, 20)
print(a)
# Solution 1: Using np.clip
print(np.clip(a, a_min=10, a_max=30))
# Solution 2: Using np.where
print(np.where(a < 10, 10, np.where(a > 30, 30, a)))


# 获取给定数组a中前5个最大值的位置。
print("".center(50, "-"))
# Solution:
print(a.argsort())
# > [18 7 3 10 15]
# Solution 2:
print(np.argpartition(-a, 5)[:5])
# > [15 10  3  7 18]
# Below methods will get you the values.
# Method 1:
a[a.argsort()][-5:]
# Method 2:
np.sort(a)[-5:]
# Method 3:
np.partition(a, kth=-5)[-5:]
# Method 4:
a[np.argpartition(-a, 5)][:5]


# 按行计算唯一值的计数。
print("".center(50, "-"))
np.random.seed(100)
arr = np.random.randint(1, 11, size=(6, 10))
# Solution


def counts_of_all_values_rowwise(arr2d):
    # Unique values and its counts row wise
    num_counts_array = [np.unique(row, return_counts=True) for row in arr2d]
    # Counts of all values row wise
    return([[int(b[a == i]) if i in a else 0 for i in np.unique(arr2d)] for a, b in num_counts_array])


# Print
print(np.arange(1, 11))
print(counts_of_all_values_rowwise(arr))

# Example 2:
arr = np.array([np.array(list('bill clinton')), np.array(
    list('narendramodi')), np.array(list('jjayalalitha'))])
print(np.unique(arr))
print(counts_of_all_values_rowwise(arr))


# 将array_of_arrays转换为扁平线性1d数组。
print("".center(50, "-"))
arr1 = np.arange(3)
arr2 = np.arange(3, 7)
arr3 = np.arange(7, 10)
array_of_arrays = np.array([arr1, arr2, arr3])
# Solution 1
arr_2d = np.array([a for arr in array_of_arrays for a in arr])
print(arr_2d)
# Solution 2:
arr_2d = np.concatenate(array_of_arrays)
print(arr_2d)
print(arr_2d.ravel())

# 计算一次性编码(数组中每个唯一值的虚拟二进制变量)
print("".center(50, "-"))
np.random.seed(101)
arr = np.random.randint(1, 4, size=6)
# Solution:


def one_hot_encodings(arr):
    uniqs = np.unique(arr)
    out = np.zeros((arr.shape[0], uniqs.shape[0]))
    for i, k in enumerate(arr):
        out[i, k-1] = 1
    return out


print(one_hot_encodings(arr))
# Method 2:
print(arr[:, None])
print((arr[:, None] == np.unique(arr)).view(np.int8))


# 为给定的数字数组a创建排名。
print("".center(50, "-"))
np.random.seed(10)
a = np.random.randint(20, size=10)
print(a)
# Solution
print(a.argsort())
print('Array: ', a)


# 创建与给定数字数组a相同形状的排名数组。
print("".center(50, "-"))
np.random.seed(10)
a = np.random.randint(20, size=[2, 5])
print(a)
# Solution
print(a.ravel().argsort().argsort().reshape(a.shape))


# 计算给定数组中每行的最大值。
print("".center(50, "-"))
np.random.seed(100)
a = np.random.randint(1, 10, [5, 3])
# Solution 1
print(np.amax(a, axis=1))
# Solution 2
print(np.apply_along_axis(np.max, arr=a, axis=1))


# 为给定的二维numpy数组计算每行的最小值。
print("".center(50, "-"))
np.random.seed(100)
a = np.random.randint(1, 10, [5, 3])
print(np.amin(a, axis=1))


# 在给定的numpy数组中找到重复的条目(第二次出现以后)，并将它们标记为True。第一次出现应该是False的。
print("".center(50, "-"))
np.random.seed(100)
a = np.random.randint(0, 5, 10)
print('Array: ', a)
# Solution
# There is no direct function to do this as of 1.13.3
# Create an all True array
out = np.full(a.shape[0], True)
# Find the index positions of unique elements
unique_positions = np.unique(a, return_index=True)[1]
# Mark those positions as False
out[unique_positions] = False
print(out)


# 从以下URL导入图像并将其转换为numpy数组。
print("".center(50, "-"))
# Import image from URL
URL = 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Denali_Mt_McKinley.jpg'
response = requests.get(URL)
# Read it as Image
I = Image.open(BytesIO(response.content))
# Optionally resize
I = I.resize([150, 150])
# Convert to numpy array
arr = np.asarray(I)
# Optionaly Convert it back to an image and show
im = PIL.Image.fromarray(np.uint8(arr))
# Image.Image.show(im)


# 从一维numpy数组中删除所有NaN值
print("".center(50, "-"))
a = np.array([1, 2, 3, np.nan, 5, 6, 7, np.nan])
print(a[~np.isnan(a)])


# 计算两个数组a和数组b之间的欧氏距离。
print("".center(50, "-"))
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])
# Solution
dist = np.linalg.norm(a - b)
print(dist)


# 找到一个一维数字数组a中的所有峰值。峰顶是两边被较小数值包围的点。
print("".center(50, "-"))
a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
doublediff = np.diff(np.sign(np.diff(a)))
print(doublediff)
peak_locations = np.where(doublediff == -2)[0] + 1
print(peak_locations)


# 从2d数组a_2d中减去一维数组b_1D，使得b_1D的每一项从a_2d的相应行中减去。
print("".center(50, "-"))
a_2d = np.array([[3, 3, 3], [4, 4, 4], [5, 5, 5]])
b_1d = np.array([1, 1, 1])
# Solution
print(a_2d - b_1d[:, None])


# 找出x中数字1的第5次重复的索引。
print("".center(50, "-"))
x = np.array([1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2])
n = 5
# Solution 1: List comprehension
[i for i, v in enumerate(x) if v == 1][n-1]
# Solution 2: Numpy version
np.where(x == 1)[0][n-1]


# 将numpy的datetime64对象转换为datetime的datetime对象
print("".center(50, "-"))
# **给定：** a numpy datetime64 object
dt64 = np.datetime64('2018-02-25 22:10:10')
# Solution
print(dt64.tolist())
# or
print(dt64.astype(datetime))


# 对于给定的一维数组，计算窗口大小为3的移动平均值。
print("".center(50, "-"))
# Solution
# Source: https://stackoverflow.com/questions/14313510/how-to-calculate-moving-average-using-numpy


def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


np.random.seed(100)
Z = np.random.randint(10, size=10)
print('array: ', Z)
# Method 1
print(moving_average(Z, n=3).round(2))
# Method 2:
# np.ones(3)/3 gives equal weights. Use np.ones(4)/4 for window size 4.
print(np.convolve(Z, np.ones(3)/3, mode='valid'))
