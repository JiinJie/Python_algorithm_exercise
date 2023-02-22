# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 19:34
# @Author  : jinjie
# @File    : HJ66_配置文件恢复.py

"""
有6条配置命令，它们执行的结果分别是：
命   令	            执   行
reset	            reset what
reset board	        board fault
board add	        where to add
board delete	    no board at all
reboot backplane	impossible
backplane abort	    install first
he he	            unknown command
"""


com_dict = {'reset': 'reset what',
            'reset board': 'board fault',
            'board add': 'where to add',
            'board delete': 'no board at all',
            'reboot backplane': 'impossible',
            'backplane abort': 'install first'
            }

while True:
    try:
        str_in = list(input().split(" "))
        if len(str_in) < 1 or len(str_in) > 2:
            print("<1 >2")
            # print("unknown command")
            break
        elif len(str_in) == 1:
            # if str_in[0] == 'reset'[0:len(str_in[0])]: #关键匹配切片是否与预计一致
            if str_in[0].startswith("reset", 0, len(str_in[0])):  # 也可以用startswith进行判断
                print(com_dict['reset'])
            else:
                print("unknown command")
        else:
            index = []
            for key in com_dict.keys():
                if key == 'reset':
                    continue
                else:
                    a = key.split()
                    if str_in[0] == a[0][0:len(str_in[0])] and str_in[1] == a[1][0:len(str_in[1])]:
                        # if str_in[0].startswith(a[0],0, len(str_in[0])) and str_in[0].startswith(a[1],0, len(str_in[0])):
                        index.append(key)

            if len(index) != 1:
                print("unknown command")
            else:
                print(com_dict[index[0]])

    except:
        break