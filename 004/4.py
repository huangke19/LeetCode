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


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n % 2 == 0:
            res = (nums1[n // 2 - 1] + nums1[n // 2]) / 2
        else:
            res = (nums1[n // 2]) / 1.0
        return res


nums1 = [1]
nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

s = Solution()
s.findMedianSortedArrays(nums1, nums2)
