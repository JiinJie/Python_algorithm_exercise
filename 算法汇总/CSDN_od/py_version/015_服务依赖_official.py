# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 10:12
# @Author  : jinjie
# @File    : 015_服务依赖_official.py

def solve_method(servers, bad):
    list_ = [string.split("-") for string in servers.split(",")]
    list_s = list(set([string.split("-")[i] for string in servers.split(",") for i in [0, 1]]))
    bad_list = bad.split(",")

    for s in bad_list:
        list_s.remove(s)

    normal_list = []
    for x in list_s:
        if not broken(list_, x, bad_list):
            normal_list.append(x)

    if len(normal_list) == 0:
        print(",")
    else:
        res = ",".join(normal_list)
        print(res)

def broken(l, s, bad_list):
    if s in bad_list:
        return True
    for i in range(len(l)):
        if l[i][0] == s and broken(l, l[i][1], bad_list):
            return True
    return False

if __name__ == "__main__":
    servers = input().strip()
    bad = input().strip()
    solve_method(servers, bad)

