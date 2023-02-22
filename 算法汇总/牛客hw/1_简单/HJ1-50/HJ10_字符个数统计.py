# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 14:07
# @Author  : jinjie
# @File    : HJ10_字符个数统计.py

"""
编写一个函数，计算字符串中含有的不同字符的个数。字符在 ASCII 码范围内( 0~127 ，包括 0 和 127 )，换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
例如，对于字符串 abaca 而言，有 a、b、c 三种不同的字符，因此输出 3 。
"""


def distin_str():
    str = ''.join(set(input()))  #先将输入的内容去重，使用set 再转为字符串，使用''.join
    temp_list = list(str)

    count = 0
    for i in temp_list:
        if 0 <= ord(i) <= 127:  #判断是否属于ASCII 使用 ord函数
            count += 1
        else:
            pass

    return count

print(distin_str())