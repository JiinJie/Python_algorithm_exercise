# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 18:05
# @Author  : jinjie
# @File    : 014_获取最大软件版本号_100.py

"""
题目
Maven版本号定义，<主版本>，<次版本>，<增量版本>·<里程碑版本>
举例3.1.4-beta其中，主版本和次版本都是必须的，主版本，次版本，增量版本由多位数字组成，可能包含前导零，里程碑版本由字
符串组成。
<主版本>，<次版本>，<增量版本>：基于数字比较
里程碑版本：基于字符串比较0，采用字典序
比较版本号时，按从左到右的顺序依次比较。基于数字比较，只需比较忽略任何前导零后的整数值。
输入2个版本号，输出最大版本号
输入
输入2个版本号，换行分割，每个版本的最大长度小于50
"""

list_a = list(input().split("."))
list_b = list(input().split("."))

# print(list_a)
# print(list_b)
if len(list_b)>len(list_a):
    list_a,list_b = list_b,list_a

for i in range(len(list_a)):
    if list_b[i] >list_a[i]:
        print(list_b)
        break
    else:
        print(list_a)
        break

