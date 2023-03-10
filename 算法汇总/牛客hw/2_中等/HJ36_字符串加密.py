# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 11:22
# @Author  : jinjie
# @File    : HJ36_字符串加密.py

"""
有一种技巧可以对数据进行加密，它使用一个单词作为它的密匙。下面是它的工作原理：首先，选择一个单词作为密匙，如TRAILBLAZERS。如果单词中包含有重复的字母，只保留第1个，将所得结果作为新字母表开头，并将新建立的字母表中未出现的字母按照正常字母表顺序加入新字母表。如下所示：
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T R A I L B Z E S C D F G H J K M N O P Q U V W X Y (实际需建立小写字母的字母表，此字母表仅为方便演示）
上面其他用字母表中剩余的字母填充完整。在对信息进行加密时，
信息中的每个字母被固定于顶上那行，并用下面那行的对应字母一一取代原文的字母(字母字符的大小写状态应该保留)。
因此，使用这个密匙， Attack AT DAWN (黎明时攻击)就会被加密为Tpptad TP ITVH。
请实现下述接口，通过指定的密匙和明文得到密文。
数据范围：1≤n≤100  ，保证输入的字符串中仅包含小写字母
"""
encode_key = str(input()).upper()
str_in = input()

res = ""

alpha_dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
temp_dict = encode_key + alpha_dict
encode_dict = ""

for i in temp_dict:
    if i in encode_dict:
        continue
    else:
        encode_dict += i
# print(encode_dict)


for i in str_in:
    # print(i)
    for j in range(len(alpha_dict)):
        # print(alpha_dict[j])
        if i == alpha_dict[j]:
            # print(i,encode_dict[j])
            res += encode_dict[j]
        elif i.upper() == alpha_dict[j]:
            # print(i.upper(),alpha_dict[j],encode_dict[j])
            res += encode_dict[j].lower()
        elif i.isalpha():
            continue
        else:
            res += i
            break

print(res)