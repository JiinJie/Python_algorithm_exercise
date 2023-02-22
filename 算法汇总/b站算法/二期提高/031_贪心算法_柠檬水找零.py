# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 17:42
# @Author  : jinjie
# @File    : 031_贪心算法_柠檬水找零.py

"""
在柠檬水摊上，每一杯柠檬水的售价为5美元。顾客排队购买，一次买一杯
每位顾客只买一杯柠檬水，然后向你付5美元、10美元或20美元。必须给每个顾客正确找零
注意：一开始你手头没有零钱
如果你能给每位顾客正确找零，返回true，否则返回false
"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if five >0 and ten >0:  #优先找零大额
                    five -= 1
                    ten -= 1
                elif five >=3:
                    five -= 3
                else:
                    return False
        return True