#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 对于位置1，存入h1*1, 如果位置2大于1，store h1*2，如果小于, store h2*2，
# 分别对每一个数计算max，最后选出最大

def LargestRectangleinHistogram(heights):
    L = 0
    n = len(heights)
    for i in range(n):
        L = max(L, heights[i])
        min_L = heights[i]
        for j in range(i + 1, n):
            min_L = min(heights[j], min_L)
            if heights[j] >= heights[i]:
                L = max(min_L * (j - i + 1), heights[j], L)
            else:
                L = max(L, min_L * (j - i + 1))
    return L


s = [2, 1, 5, 6, 2, 3]
print(LargestRectangleinHistogram(s))
