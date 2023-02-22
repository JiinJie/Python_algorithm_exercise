# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 12:12
# @Author  : jinjie
# @File    : 007_★特异性双端队列_100.py

"""
题目
有一个特异性的双端队列，该队列可以从头部到尾部添加数据，但是只能从头部移除数据。
·小A一次执行2n个指令往队列中添加数据和移除数据，其中n个指令是添加数据（可能从头部也可以从尾部添加）
·依次添加1到n，n个指令是移出数据
现在要求移除数据的顺序为1到n，
为了满足最后输出的要求，
·小A可以在任何时候调整队列中的数据的顺序
请问，小A最少需要调整几次才能满足移除数据的顺序正好是1到n
"""
from collections import deque


def solve_method(commands):
    times = 0
    in_ = 0
    out = 0
    linked_list = deque()

    for command in commands:
        c = command[0]
        if c == 'h':
            linked_list.appendleft(in_ + 1)
            in_ += 1
        elif c == 't':
            linked_list.append(in_ + 1)
            in_ += 1
        else:
            if linked_list[0] != out + 1:
                times += 1
                linked_list = deque(sorted(linked_list))
            linked_list.popleft()
            out += 1

    return times


n = int(input().strip())
commands = [input().strip() for i in range(n * 2)]
res = solve_method(commands)
print(res)

