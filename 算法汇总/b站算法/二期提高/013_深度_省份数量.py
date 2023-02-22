# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 15:03
# @Author  : jinjie
# @File    : 013_深度_省份数量.py
"""
有n个城市，其中一些彼此相连，另一些没有相连如果城市a与城市b直接相连，且城市b与城市c直接相连，那么城市a与城市c间接相连
省份是一组直接或间接相连的城市，组内不含其他没有相连的城市给你一 n * n 的矩阵 isConnected，
其中isConnected[i][j]=1表示第i个城市和第j个城市直接相连，而 isconnected[i][j]=0 表示二者不直接相连
返回矩阵中的省份数量
"""



#from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited[i] = 1 #将当前城市进行标记，visited存放所有城市是否被访问的状态
            for j in range(n): #j来遍历每个城市,i表示是否与当前城市相连
            # j是行,i是列，每一行是一个城市的数据
                if isConnected[i][j] ==1 and not visited[j]:
                    dfs(j) #如果当前城市是关联城市且未被访问过，继续深度搜索当前城市的关联城市
        n = len(isConnected)
        #初始化一个访问数组,长度为所有城市数
        visited = [0] *n
        count = 0 #统计省份
        for i in range(n): #遍历城市数
            if not visited[i]:
                count += 1
                dfs(i)  #如果没有被访问则省份加1，同时对该城市进行深度遍历
        return count