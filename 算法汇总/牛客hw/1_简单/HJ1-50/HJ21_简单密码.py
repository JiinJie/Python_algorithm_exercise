# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 15:01
# @Author  : jinjie
# @File    : HJ21_简单密码.py

"""
现在有一种密码变换算法。
九键手机键盘上的数字与字母的对应： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0，把密码中出现的小写字母都变成九键键盘对应的数字，如：a 变成 2，x 变成 9.
而密码中出现的大写字母则变成小写之后往后移一位，如：X ，先变成小写，再往后移一位，变成了 y ，例外：Z 往后移是 a 。
数字和其它的符号都不做变换。
"""


list1 = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
get_str = input()
result = ''

for i in get_str:
    # 如果是字母
    if i.isalpha():  # 判断是否为字母
        # 如果是大写
        if i.isupper():  #判断是否为大写
            if i == 'Z':
                result += 'a'
            else:
                result += chr(ord(i.lower())+1)
        # 如果不是大写
        else:
            for j in list1:
                if i in j:
                    result += str(list1.index(j)+2)  #默认索引是0，而按键从2开始，需要+2
                    print(list1.index(j))
                    break
    else:
        result += i

print(result)