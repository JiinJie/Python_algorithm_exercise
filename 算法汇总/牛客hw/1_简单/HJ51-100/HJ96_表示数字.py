# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 11:19
# @Author  : jinjie
# @File    : HJ96_表示数字.py


"""
将一个字符串中所有的整数前后加上符号“*”，其他字符保持不变。连续的数字视为一个整数。
数据范围：字符串长度满足 1≤n≤100
"""

import re

while True:
    try:
        str_in = input()
        res = re.sub('(\d+)', '*\g<1>*',str_in) #匹配所有字符串中的数字，并将前后加上"*"
        print(res)
    except:
        break

"""
re.sub(pattern, repl, string, count=0, flags=0)
参数：

pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
"""
"""
#元字符
\d 代表是一个0-9的数字字符
[0-9] 代表0-9的一个数
\D 除0-9的字符
^ 匹配字符串开始
$ 匹配字符串结束
. 匹配除换行符外的字符
^ 表示脱字符

#量词（修饰前面（挨着的那个）的字符出现的次数）
'+' 代表是1或n次 <=> {1, }
'*' 代表0或n次 <=> {0, }
'?' 代表0或1次 <=> {0, 1}
'.' 表示匹配除"\n"(换行符)和"\r"（回车符）之外的任何单个字符
{5} 确定几次

#模式修饰符
'g' 全局匹配，找全部符合条件的字符
'i' 忽略大小写

#子项和引用和捕获
var reg = /(-)([a-z])/
简单理解子项就是分组，看括号，左至右1，2，3...
"""