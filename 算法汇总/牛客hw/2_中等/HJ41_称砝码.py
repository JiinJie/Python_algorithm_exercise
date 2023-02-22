# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 12:23
# @Author  : jinjie
# @File    : HJ41_称砝码.py
#
# """
# 现有n种砝码，重量互不相等，分别为 m1,m2,m3…mn ；
# 每种砝码对应的数量为 x1,x2,x3...xn 。
# 现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
# 注：称重重量包括 0
# """
#
# """
# 输入描述：
# 对于每组测试数据：
# 第一行：n --- 砝码的种数(范围[1,10])
# 第二行：m1 m2 m3 ... mn --- 每种砝码的重量(范围[1,2000])
# 第三行：x1 x2 x3 .... xn --- 每种砝码对应的数量(范围[1,10])
# 输出描述：
# 利用给定的砝码可以称出的不同的重量数
# """
#
# """
# 输入：2
# 1 2
# 2 1
# 输出：5
# 说明：
# 可以表示出0，1，2，3，4五种重量。   """


# 无注释版
str_cart = int(input())
str_weight = list(map(int,input().split()))
str_num = list(map(int,input().split()))

amount = []
weights = {0,}

for i in range(str_cart):
    for j in range(str_num[i]):
        amount.append(str_weight[i])
for i in amount:
    for j in list(weights):
        weights.add(i+j)

print(len(weights))


# 注释版
# str_cart = int(input())
# str_weight = list(map(int,input().split()))
# str_num = list(map(int,input().split()))
str_cart = 3
str_weight = [1,2,5]
str_num = [2,2,1]
amount = []
weights = {0,}

# 使用n种不同砝码进行组合
for i in range(str_cart):
    #amount.extend([int(str_weight[i])]*int(str_num[i]))
    for j in range(str_num[i]):  # 每种砝码选择几个
        amount.append(str_weight[i])
        print("-"*10)
    print(f"当前amount值为{amount}")
# 输出amount为砝码重量的列表
print(amount)


for i in amount: #遍历每个砝码
    for j in list(weights):  #重复遍历当前已经获得的重量情况
        #print(f"----{weights}")
        print(i+j)  #将之前的重量加上该砝码的重量，查看是否出现新的重量
        weights.add(i+j)
print(weights)  #可能出现的重量总和
print(len(weights))



