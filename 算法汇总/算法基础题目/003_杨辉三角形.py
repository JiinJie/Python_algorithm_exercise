# -*- coding: utf-8 -*-
# @Time    : 2023/2/8 11:53
# @Author  : jinjie
# @File    : 003_杨辉三角形.py

"""
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
"""
# 打印杨辉三角

# 方法一：逻辑法
L = [] # 创建一个空列表
# for i in range(1, 4): # 控制行 一共创建10行
#     list = [] # 创建一个空列表
#     for j in range(1, i+1): #控制列
#         list.append(0) # 将数字添加到空列表当中
#     list[0] = 1 #每一行的第一个为0
#     list[-1] = 1 #每一行的最后一个为0
#     L.append(list)
#     if len(list) > 2:  # 如果list的长度大于2
#         for k in range(len(list)): # 遍历len(list)的长度
#             if 0 < k < len(list)-1:
#                 list[k] = L[-2][k-1] + L[-2][k] # 计算出list的值，也就是其上两个值的临近元素的加总
# for a in L:
#     for b in a:
#         print(b, end=' ')
#     print()


# 方法二：公式法【推荐】
N = [1]
for i in range(3):  #i从0开始，i-1结束
    #print(N)
    N.append(0)
    # 当i= 0开始时
    # 第一个值new_N[0]的1 是N[0]+N[-1] = 1+0 = 1
    # 第二个值是 new_N[1]的值是2 new_N[0]+N[-1] = 1。
    # 此时j = 1,结束循环
    N = [N[k] + N[k-1] for k in range(i+2)]  #每次输出每一行的结果
    # 在for循环时，N.append(N[k] + N[k-1])  因此最后一个空值 new_N[-1] = N[k] + N[k-1]
