# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 14:10
# @Author  : jinjie
# @File    : HJ16_购物单.py

"""
王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，
下表就是一些主件与附件的例子：
----------------------------
主件	            附件
电脑	        打印机，扫描仪
书柜	            图书
书桌	          台灯，文具
工作椅	        无
----------------------------
如果要买归类为附件的物品，必须先买该附件所属的主件，且每件物品只能购买一次。
每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。
王强查到了每件物品的价格（都是 10 元的整数倍），而他只有 N 元的预算。除此之外，他给每件物品规定了一个重要度，用整数 1 ~ 5 表示。他希望在花费不超过 N 元的前提下，使自己的满意度达到最大

满意度是指所购买的每件物品的价格与重要度的乘积的总和，
假设设第i件物品的价格为v[i]重要度为w[i]，共选中了k件物品,编号依次为 j1,j2,...,jk，
则满意度为：v[j1]*w[j1]+v[j2]*w[j2]+...+v[jk]*w[jk]
请你帮助王强计算可获得的最大的满意度。
"""
"""
输入描述：
输入的第 1 行，为两个正整数N，m，用一个空格隔开：
（其中 N （ N<32000 ）表示总钱数， m （m <60 ）为可购买的物品的个数。）
从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q
（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。
如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）
输出描述：
 输出一个正整数，为张强可以获得的最大的满意度。
"""
"""
示例1
输入：1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0

输出：2200
"""


# 解1--基础版【dp使用二维数组】
n,m = map(int,input().split())  # 输入两个参数，允许的总价格，允许的总件数
primary,annex = {},{}

for i in range(1,m+1):
    x,y,z = map(int,input().split())  #输入的三个参数 价格，重要度，主附件属性
    if z == 0: #判断是否为主件
        primary[i] = [x,y]  # 添加至主件列表中
    else: #不是主件
        if z in annex:  #z已经存在，表明列表中已有附件，当前附件为第二个
            annex[z].append([x,y]) #添加至附件列表中
        else: #z不存在,这是第一个附件
            annex[z] = [[x,y]]


m = len(primary)
dp = [[0]*(n+1) for _ in range(m+1)]  #创建dp的二维数组
w,v = [[]],[[]]

for key in primary:
    w_temp, v_temp = [], []
    w_temp.append(primary[key][0])#1、主件
    v_temp.append(primary[key][0]*primary[key][1])  #满意度
    if key in annex:#存在主件
        w_temp.append(w_temp[0]+annex[key][0][0])#2、主件+附件1
        v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1]) #满意度
        if len(annex[key])>1:#存在两主件
            w_temp.append(w_temp[0]+annex[key][1][0])#3、主件+附件2
            v_temp.append(v_temp[0]+annex[key][1][0]*annex[key][1][1])
            w_temp.append(w_temp[0]+annex[key][0][0]+annex[key][1][0])#3、主件+附件1+附件2
            v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1]) #满意度
    w.append(w_temp)
    v.append(v_temp)
for i in range(1,m+1):
    for j in range(10,n+1,10):#物品的价格是10的整数倍
        max_i = dp[i-1][j]
        for k in range(len(w[i])):
            if j-w[i][k]>=0:
                max_i = max(max_i, dp[i-1][j-w[i][k]]+v[i][k])
        dp[i][j] = max_i
print(dp[m][n])


