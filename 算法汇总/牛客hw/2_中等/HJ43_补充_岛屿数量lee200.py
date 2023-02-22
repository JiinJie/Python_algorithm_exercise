# -*- coding: utf-8 -*-
# @Time    : 2023/2/14 15:52
# @Author  : jinjie
# @File    : HJ43_补充_岛屿数量lee200.py

"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

"""
"""
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 递归当前格子相关联的上下左右格子
        def dfs(grid, r, c):
            if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):  #如果上下左右没有格子
                return
            if grid[r][c] != "1": #如果该格子不是岛屿（即格子的值为0）
                return  # 注意题目这里输入的是字符"0",“1”
            grid[r][c] = "2"  #将其赋值为2作为区分，避免重复计算
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c - 1)
            dfs(grid, r, c + 1)
            return 1  # 是岛屿,则返回1

        # 定义结果
        res = 0
        # 遍历扫描所有格子
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    res += dfs(grid, r, c)  # 累加岛屿的数量
        return res


grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

res = Solution().numIslands(grid2)
print(res)
