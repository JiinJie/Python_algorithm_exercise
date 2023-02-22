# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 15:54
# @Author  : jinjie
# @File    : 014_广度_省份数量.py


# 广度优先
from collections import deque
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        #初始化标记数组
        visited = [0]*n
        count = 0
        q = deque()

        #遍历城市，开始搜索
        for i in range(n):
            if not visited[i]:
                # 更新变量
                visited[i] = 1
                count += 1
                q.append(i)

                while q:
                    u = q.popleft()
                    for v in range(n):  #遍历所有的城市数
                        if isConnected[u][v] ==1 and not visited[v]:
                            visited[v] =1
                            q.append(v)
        return count