# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 11:33
# @Author  : jinjie
# @File    : 018_栈与队列_字符串解码.py

"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
"""
from builtins import str

# 方法一：使用辅助栈
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0  #stack存放入栈数据 res为出栈数据 multi存放倍数
        for c in s:
            if c == '[':
                stack.append([multi, res])
                #print(stack)
                res, multi = "", 0
            elif c == ']':  #如果闭合，则取出stack内容添加至res中
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res


# 方法二：使用递归，迭代输出
# class Solution2:
#     def decodeString(self, s: str) -> str:
#         def inner(s, i):
#             res, multi = "", 0
#             while i < len(s):
#                 if '0' <= s[i] <= '9':
#                     multi = multi * 10 + int(s[i])  #先读取的*10 最终得出倍数
#                 elif s[i] == '[':
#                     i, tmp = inner(s, i + 1)  #递归，直到没有'['
#                     res += multi * tmp  #获取内层的结果，然后将倍数置零
#                     multi = 0
#                 elif s[i] == ']':
#                     return i, res
#                 else:
#                     res += s[i]
#                 i += 1
#             return res
#
#         return inner(s, 0)




if __name__ == '__main__':
    str = "zzz3[a2[c]]"
    a = Solution().decodeString(str)
    print(a)