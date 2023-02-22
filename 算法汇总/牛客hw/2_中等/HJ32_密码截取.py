# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 22:04
# @Author  : jinjie
# @File    : HJ32_密码截取.py

# """
# Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，
# 比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。
# 比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。
# 因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
# Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
# """




# print(str_in[2])
# print(str_in[2:5])

#str_in = 'ABBBA'
# str_in = 'ABQPBNCBAB'
str_in = input()
res = []


for i in range(len(str_in)):
    for j in range(1,len(str_in)):
        if str_in[j] == str_in[i] and str_in[i+1:j] == str_in[j-1:i:-1]:
            # 判断最外层是否一致，一致后再判断内部字符串倒序后是否相等
            res.append(len(str_in[i:j+1])) #list[2:5] 表示从第三个到第五个，如果根据索引获取需要+1

print(max(res))