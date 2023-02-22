# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 16:43
# @Author  : jinjie
# @File    : HJ20_密码验证合格程序.py

# 统计字符串，不能有长度大于2的包含公共元素的子串重复
"""
-----------------------------------------
# 长度为4的公共字串肯定包含长度为3的多个公共字串，
#因此直接计算字符串中是否包含长度为3的子字符串即可
-----------------------------------------
str_in = input()
for i in range(len(str_in) - 3):
    if len(str_in.split(str_in[i:i + 3])) >= 3:  #判断字符串是否有重复子串
        return 0

"""

"""
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）
"""


def check(str_in):
    if len(str_in) < 8:
        return 0
    flag = [0, 0, 0, 0]  #用于记录复杂度
    for i in str_in:
        if i.isupper():
            flag[0] = 1
        elif i.islower():
            flag[1] = 1
        elif i.isdigit():
            flag[2] = 1
        else:
            flag[3] = 1

    if sum(flag) < 3:
        return 0
    for i in range(len(str_in) - 3):
        if str_in.count(str_in[i:i + 3]) > 1: #使用计数判断是否有重复
        #if len(str_in.split(str_in[i:i + 3])) >= 3:  #使用截断，判断字符串是否有重复子串
            return 0

    return 1


while True:
    try:
        print("OK" if check(input()) else "NG")
    except:
        break