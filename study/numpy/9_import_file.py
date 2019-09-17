# -*- coding: utf-8 -*-

import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

# Print the first 3 rows
print(iris[:3])


print("".center(50, "-"))
species = np.array([row[4] for row in iris])
print(species[:5])


print("".center(50, "-"))
# Method 1: Convert each row to a list and get the first 4 items
iris_2d = np.array([row.tolist()[:4] for row in iris])
print(iris_2d[:4])
# Alt Method 2: Import only the first 4 columns from source url
iris_2d = np.genfromtxt(
    url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
print(iris_2d[:4])


# 求出鸢尾属植物萼片长度的平均值、中位数和标准差(第1列)
print("".center(50, "-"))
mu, med, sd = np.mean(iris_2d[:, 0]), np.median(
    iris_2d[:, 0]), np.std(iris_2d[:, 0])
print(mu, med, sd)


# 创建一种标准化形式的鸢尾属植物间隔长度，其值正好介于0和1之间，这样最小值为0，最大值为1。
sepallength = iris_2d[:, 0]
Smax, Smin = sepallength.max(), sepallength.min()
print("".center(50, "-"))
S = (sepallength - Smin)/sepallength.ptp()  # Thanks, David Ojeda!
print(S)


# 找到鸢尾属植物数据集的第5和第95百分位数
print("".center(50, "-"))
print(np.percentile(sepallength, q=[5, 95]))


# 在iris_2d数据集中的20个随机位置插入np.nan值
print("".center(50, "-"))
# Method 1
i, j = np.where(iris_2d)
# i, j contain the row numbers and column numbers of 600 elements of iris_x
np.random.seed(100)
iris_2d[np.random.choice((i), 20), np.random.choice((j), 20)] = np.nan
print(iris_2d)
# Method 2
np.random.seed(100)
iris_2d[np.random.randint(150, size=20),
        np.random.randint(4, size=20)] = np.nan
# Print first 10 rows
print(iris_2d[:10])


# 在iris_2d的sepallength中查找缺失值的数量和位置（第1列）
print("".center(50, "-"))
# Solution
print(np.isnan(iris_2d[:, 0]))
print("Number of missing values: \n", np.isnan(iris_2d[:, 0]).sum())
print("Position of missing values: \n", np.where(np.isnan(iris_2d[:, 0])))


# 过滤具有petallength（第3列）> 1.5 和 sepallength（第1列）< 5.0 的iris_2d行
print("".center(50, "-"))
condition = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)
print(iris_2d[condition])


# 选择没有任何nan值的iris_2d行
print("".center(50, "-"))
# Solution
# No direct numpy function for this.
# Method 1:
any_nan_in_row = np.array([~np.any(np.isnan(row)) for row in iris_2d])
print(iris_2d[any_nan_in_row][:5])
# Method 2: (By Rong)
print(np.sum(np.isnan(iris_2d), axis=1))
print(iris_2d[np.sum(np.isnan(iris_2d), axis=1) == 0][:5])


# 在iris_2d中找出SepalLength（第1列）和PetalLength（第3列）之间的相关性
print("".center(50, "-"))
iris_2d = iris_2d[any_nan_in_row][:5]
print(np.corrcoef(iris_2d[:, 0], iris_2d[:, 2]))


# 找出鸢尾属植物物种中的独特值和独特值的数量
# Solution
# Extract the species column as an array
species = np.array([row.tolist()[4] for row in iris])
# Get the unique values and the counts
print(np.unique(species, return_counts=True))


# 将iris_2d的花瓣长度（第3列）加入以形成文本数组
print("".center(50, "-"))
# Bin petallength
petal_length_bin = np.digitize(iris[:, 2].astype('float'), [0, 3, 5, 10])
# Map it to respective category
label_map = {1: 'small', 2: 'medium', 3: 'large', 4: np.nan}
petal_length_cat = [label_map[x] for x in petal_length_bin]
# View
print(petal_length_cat[:4])


# 在iris_2d中为卷创建一个新列，其中volume是（pi x petallength x sepal_length ^ 2）/ 3
print("".center(50, "-"))
# Solution
# Compute volume
sepallength = iris[:, 0].astype('float')
petallength = iris[:, 2].astype('float')
volume = (np.pi * petallength * (sepallength ** 2))/3
# Introduce new dimension to match iris_2d's
volume = volume[:, np.newaxis]
# Add the new column
out = np.hstack([iris, volume])
print(out[:4])


# 第二长的物种setosa的价值是多少
print("".center(50, "-"))
# Solution
# Get the species and petal length columns
petal_len_setosa = iris[iris[:, 4] == b'Iris-setosa', [2]].astype('float')
# Get the second last value
print(np.sort(petal_len_setosa))
print(np.unique(np.sort(petal_len_setosa))[-2])


# 根据sepallength列对虹膜数据集进行排序。
print("".center(50, "-"))
# Sort by column position 0: SepalLength
print(iris[:, 0].argsort())
print(iris[iris[:, 0].argsort()][:20])


# 在鸢尾属植物数据集中找到最常见的花瓣长度值（第3列）。
print("".center(50, "-"))
# Solution:
vals, counts = np.unique(iris[:, 2], return_counts=True)
print(vals[np.argmax(counts)])


# 在虹膜数据集的petalwidth第4列中查找第一次出现的值大于1.0的位置。
print("".center(50, "-"))
print(np.argwhere(iris[:, 3].astype(float) > 1.0)[0])


# 创建按分类变量分组的行号。使用以下来自鸢尾属植物物种的样本作为输入。
print("".center(50, "-"))
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
species = np.genfromtxt(url, delimiter=',', dtype='str', usecols=4)
species_small = np.sort(np.random.choice(species, size=20))
print([i for val in np.unique(species_small)
       for i, grp in enumerate(species_small[species_small == val])])


# 根据给定的分类变量创建组ID。使用以下来自鸢尾属植物物种的样本作为输入。
print("".center(50, "-"))
# Solution:
output = [np.argwhere(np.unique(species_small) == s).tolist()[0][0] for val in np.unique(
    species_small) for s in species_small[species_small == val]]
# Solution: For Loop version
output = []
uniqs = np.unique(species_small)
for val in uniqs:  # uniq values in group
    for s in species_small[species_small == val]:  # each element in group
        groupid = np.argwhere(uniqs == s).tolist()[0][0]  # groupid
        output.append(groupid)
print(output)


# 在二维数字数组中查找按分类列分组的数值列的平均值
print("".center(50, "-"))
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
# Solution
# No direct way to implement this. Just a version of a workaround.
numeric_column = iris[:, 1].astype('float')  # sepalwidth
grouping_column = iris[:, 4]  # species
# List comprehension version
print([[group_val, numeric_column[grouping_column == group_val].mean()]
       for group_val in np.unique(grouping_column)])
# For Loop version
output = []
for group_val in np.unique(grouping_column):
    output.append(
        [group_val, numeric_column[grouping_column == group_val].mean()])
print(output)
