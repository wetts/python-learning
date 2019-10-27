# -*- encoding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2019/10/21 12:48:06
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   利用回溯法求解如下迷宫问题。
'''

# here put the import lib
import queue

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
directions = [lambda x, y: (x + 1, y),
              lambda x, y: (x - 1, y),
              lambda x, y: (x, y - 1),
              lambda x, y: (x, y + 1),
              lambda x, y: (x - 1, y - 1),
              lambda x, y: (x + 1, y - 1),
              lambda x, y: (x + 1, y + 1),
              lambda x, y: (x - 1, y + 1), ]


class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def print_path(self):
        n = self
        arr = [(n.x, n.y)]
        while n.parent:
            n = n.parent
            arr.append((n.x, n.y))

        print(" -> ".join([str(n) for n in arr[::-1]]))


def find_path(x1, y1, x2, y2):
    stack = queue.LifoQueue()
    stack.put(Node(x1, y1))
    maze[x1][y1] = -1
    while not stack.empty():
        n = stack.get()
        x = n.x
        y = n.y
        if x == x2 and y == y2:  # 到达终点
            return True, n
        for dr in directions:
            next_node = dr(x, y)
            if maze[next_node[0]][next_node[1]] == 0:  # 该位置可走
                node = Node(next_node[0], next_node[1])
                node.set_parent(n)
                stack.put(node)
                maze[x][y] = -1

    return False, None


if __name__ == "__main__":
    f, p = find_path(1, 1, 8, 8)
    if f:
        print('找到了迷宫路径，路径如下')
        p.print_path()
    else:
        print('没有找到迷宫路径')
