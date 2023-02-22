# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 17:35
# @Author  : jinjie
# @File    : 013_括号检查_100.py

"""
题目
现有一字符串仅由'(',')','{','}','[',']' 六种括号组成，若字符串满足以下条件之一，则为无效字符串
1·任意类型的左右括号数量不相等
2，存在未按正确顺序（先左后右）闭合的括号，
要求：
输出括号的最大嵌套深度
若字符串无效则输出0
"""




def check_char(str_in):
    stack = []
    deeps = []
    deep = 0
    for i in str_in:
        if str_in[0] in( ')','}',']'):
            return 0
        elif i in ( '(','{','['):
            deeps.append(deep)
            deep = 0
            stack.append(i)
        elif i == ')':
            if stack.pop() == "(":
                deep += 1
            else:
                return 0
        elif i == "}":
            if stack.pop() == "{":
                deep += 1
            else:
                return 0
        elif i == "]":
            if stack.pop() == "[":
                deep += 1
            else:
                return 0
    deeps.append(deep)
    return deeps

str_in = input()
if check_char(str_in) == 0:
    print(0)
else:
    print(max(check_char(str_in)))
