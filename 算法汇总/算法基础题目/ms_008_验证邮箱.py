# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 16:18
# @Author  : jinjie
# @File    : ms_008_验证邮箱.py


"""
有写公司会要求能写一小段程序出来，如题：
写一个小程序：控制台输入邮箱地址（格式为 username@companyname.com），
程序识别用户名和公司名后，将用户名和公司名输出到控制台。
要求：
1. 校验输入内容是否符合规范（xx@yy.com）, 如是进入下一步，如否则抛出提
示"incorrect email format"。注意必须以.com 结尾
2. 可以循环“输入--输出判断结果”这整个过程
3. 按字母 Q（不区分大小写）退出循环，结束程序

"""

import re
import sys


def vaildate_email(value):
    a = re.match(r'^[0-9a-zA-Z\_\-]*@[0-9a-zA-Z]+(\.com)$', value)
    if a:
        split_value = re.split('@|\.',value)
        #print(split_value)
        username = split_value[0]
        compname = split_value[1]
        print(username,compname)
        return True
    else:
        print("incorrect email format")
        return False

input_value = input("请输入：")

while 1:
    if input_value == 'q' or input_value == 'Q':
        print("程序正在退出")
        sys.exit()

    else:
        if not vaildate_email(input_value):
            break
    print("验证成功，等待验证下一个")

    input_value = input("请输入：")




