# -*- coding: utf-8 -*-


def triangle():
    arr = [1]
    while True:
        yield arr
        arr.append(0)
        arr = [arr[i]+arr[i-1] for i in range(len(arr))]


if __name__ == '__main__':
    a = 0
    for t in triangle():
        print(t)
        a += 1
        if a == 10:
            break
