# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 14:30
# @Author  : jinjie
# @File    : basic_001_创建一个二维数组.py
from pprint import pprint

n = 8
m = 8

dp = [[0]*(n+1) for _ in range(m+1)]

pprint(dp)