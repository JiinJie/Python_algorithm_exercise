# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 20:37
# @Author  : jinjie
# @File    : 003_字母计数.py

"""
题目
给出一个只包含字母的字符串，
不包含空格，统计字符串中各个子字母（区分大小写）出现的次数，
并按照字母出欠数从大到小的顺序输出各个字母及其出欠数，
如果次数相同，按照自然顺序排序：且小写字母在大写字母之前。
输入
输入一行仅包含字母的字符串
输出
按照字母出现欠数从大到小的顺序输出各个字母和字母次数，
用英文分号分割，
汪意末尾的分号，字母和次数中间用英文冒号分隔
"""

# 方法一：使用hash表
str_in = input()
temp_dict = {}

for i in str_in:
    if temp_dict.get(i):
        temp_dict[i] += 1
    else:
        temp_dict[i] = 1

res = sorted(temp_dict.items(),key=lambda item: (-item[1], (ord(item[0]) < 95), item[0])) #对item做三次排序（value降序排列，按照大小写排序，再按照key正序排）
# test_data_1=sorted(dict_data.items(),key=lambda x:x[0]) 字典按key正序排
#print(res)

for key,value in res:
    print(f"{key};{value}",end=";")


# 方法二：使用counter
# from collections import Counter
#
#
# def solve_method(line: str) -> None:
#     char_counter = Counter(line)
#     char_count_pairs = sorted(
#         char_counter.items(),
#         key=lambda item: (-item[1], (ord(item[0]) < 95), item[0])
#     )
#     for char, count in char_count_pairs:
#         print(f"{char}:{count};", end="")
#     print()
#
#
# def main() -> None:
#     line = input().strip()
#     solve_method(line)
#
#
# if __name__ == '__main__':
#     main()
