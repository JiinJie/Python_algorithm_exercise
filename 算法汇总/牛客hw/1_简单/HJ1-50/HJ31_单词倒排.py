# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 19:01
# @Author  : jinjie
# @File    : HJ31_单词倒排.py

# """
# 对字符串中的所有单词进行倒排。
# 说明：
# 1、构成单词的字符只有26个大写或小写英文字母；
# 2、非构成单词的字符均视为单词间隔符；
# 3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符
# 4、每个单词最长20个字母
# """



str_in = '$bo*y gi!r#l'

temp_str = ""
res = ""
for i in str_in:
    if i.isalpha():
        print(i)
        temp_str += i
    else:
        temp_str += ' '
        # if temp_str[-1] == ' ':
        #     pass
        # else:
        #     temp_str += ' '

temp_list = list(temp_str.split(' '))
for i in range(len(temp_list)):
    res =res + str(temp_list.pop())+" "
print(res)
