# -*- coding: utf-8 -*-
# @Time    : 2023/2/10 11:30
# @Author  : jinjie
# @File    : HJ85_最长回文子串.py


# """
# 给定一个仅包含小写字母的字符串，求它的最长回文子串的长度。
# 所谓回文串，指左右对称的字符串。
# 所谓子串，指一个字符串删掉其部分前缀和后缀（也可以不删）的字符串
# 数据范围：字符串长度1≤s≤350
# 进阶：时间复杂度：O(n) ，空间复杂度：O(n)
# """
str_in = 'cdabbacc'
#str_in = input()
res = 0
for i in range(len(str_in)):
    for j in range(len(str_in)):
        temp_str = str_in[i:j+1] #遍历所有子串
        # temp_str[::-1]是逆序排列str
        if temp_str == temp_str[::-1] and j-i+1 >res:  #避免结果超过当前字串的长度最大值
            res = j-i+1
        else:
            continue

print(res)

