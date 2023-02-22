# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 14:18
# @Author  : jinjie
# @File    : HJ43_迷宫问题.py

"""
定义一个二维数组 N*M ，如 5 × 5 数组下所示：

int maze[5][5] = {
0, 1, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 1, 0,
};

它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，
要求编程序找出从左上角到右下角的路线。入口点为[0,0],既第一格是可以走的路。
"""

"""测试入参
5 5
0 1 0 0 0
0 1 1 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
"""



#### 深度优先算法
def dfs(i, j):
    # 初始化一个方向数组，用于判断上下左右位置
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
# 上（0， -1）
# 下（0， 1）
# 左（-1， 0）
# 右（1， 0）
    if i == m - 1 and j == n - 1:  # 如果到达终点则返回
        for pos in route:
            print(f"({pos[0]},{pos[1]})")  #如：输出的是（1，0） 即maze[1][0] 表示的是第二行第一个，即 x=0,y=1
        return

    for k in range(4): #对应四个方向
        x = i + dx[k]
        y = j + dy[k]
        if x >= 0 and x < m and y >= 0 and y < n and maze[x][y] == 0:  # 如果没到终点且当前位置未走过
            maze[x][y] = 1  # 将当前位置置为已走过
            route.append((x, y))  # 路径添加当前位置到列表中
            dfs(x, y)  # 回溯位置
            maze[x][y] = 0  # 回溯时将其再次置为0
            route.pop()  # 将最后添加的位置移除（因为没有到达终点，且为死路）
    else:
        return



while True:
    try:
        m, n = list(map(int, input().split()))
        maze = []

        for _ in range(m):
            s = list(map(int, input().split()))
            maze.append(s)

        route = [(0, 0)]
        maze[0][0] = 1
        dfs(0, 0)

    except:
        break


