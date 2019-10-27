# -*- encoding: utf-8 -*-
'''
@File    :   2.py
@Time    :   2019/10/21 12:48:29
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   利用回溯法求解八皇后问题。
'''

# here put the import lib
import queue


def conflict(board: list, x: int, y: int):
    i = 0
    while i < x:
        if abs(y - board[i]) in (0, abs(x - i)):
            return True
        i += 1
    return False


def queens(board):
    result = []
    b_len = len(board)
    stack = queue.LifoQueue()
    stack.put((0, 0))
    while not stack.empty():
        i, j = stack.get()
        if not conflict(board, i, j):
            board[i] = j
            if i >= b_len - 1:  # i到达最后一行表明已经有了结果
                # print(board)
                result.append(board.copy())
            else:
                if j < b_len - 1:    # 把本位置右边一格入栈，但是如果本位置已经是行末尾，就跳过
                    stack.put((i, j+1))
                stack.put((i+1, 0))    # 下一行第一个位置入栈，准备开始下一行的扫描
        elif j < b_len - 1:
            stack.put((i, j+1))    # 对于未通过检验的情况，自然右移一格即可

    return result


if __name__ == "__main__":
    r = queens([0] * 8)
    print(r)
    print('有 %d 种方法' % len(r))
