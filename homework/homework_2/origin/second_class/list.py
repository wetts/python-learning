list = [i for i in range(10)]
# print(list)
# print(list[-1])
# print(list[0:5])
# print(list[::3])

string = 'sdd'
from collections import Iterable, Iterator

# print(type(string))
# print(isinstance(string,Iterable))
for i in string:
    print(i)

# print(string[-1])

long_str = '''
hsad
fwe
'''

# print(len(long_str))
for i in long_str:
    print(ord(i))

# \0是文件结束符

li = [i ** 2 for i in range(10)]
print(li)

# li=[[i**2 for i  in range(10)]*2]
# print(li)

# print(isinstance(li, Iterator))
# iter_li = iter(li)
#
# print(iter_li)
# print(next(iter_li))
# print(next(iter_li))
# for i in iter_li:
#     print(i)
#
# # print(next(iter_li))
# for i in iter_li:
#     print(i)
#
# iter_new = iter_li
# for j in iter_new:
#     print('new iter:', j)
#
# generator_li = (x for x in range(10))
# print(generator_li)
# print(isinstance(generator_li, Iterable))
# for i in generator_li:
#     print(i)


def fib(max):
    '''
    1 1 2 3 5 8
    :param max:
    :return:
    '''
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n += 1
        print(b)
    return 'done'

fib(10)
