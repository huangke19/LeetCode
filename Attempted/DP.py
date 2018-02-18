#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1. 检查先决条件
2. 定义子程序要解决的问题
3. 为子程序命名
4. 决定如何测试子程序
5. 在标准库中搜寻可用的功能
6. 考虑错误处理
7. 考虑效率问题
8. 研究算法和数据类型
9. 编写伪代码
    1. 首先简要地用一句话来写下该子程序的目的，
    2. 编写很高层次的伪代码
    3. 考虑数据
    4. 检查伪代码
10. 在伪代码中试验一些想法，留下最好的想法
'''

arr = [1, 2, 4, 1, 7, 8, 3, 9, 9]


def rec_opt(arr, i):
    if i == 0:
        return arr[0]
    if i == 1:
        return max(arr[0], arr[1])
    else:
        a = rec_opt(arr, i - 1)
        b = rec_opt(arr, i - 2) + arr[i]
        return max(a, b)


print(rec_opt(arr, 8))

import numpy as np


def dp_opt(arr):
    opt = np.zeros(len(arr))
    opt[0] = 1
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        A = opt[i - 2] + arr[i]
        B = opt[i - 1]
        opt[i] = max(A, B)
    return opt[len(arr) - 1]


print(dp_opt(arr))

arr2 = [4, 1, 1, 9, 1]
print(dp_opt(arr))
print(rec_opt(arr2, 5))
print(dp_opt(arr2))
