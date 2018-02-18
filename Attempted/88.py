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
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        r = []
        while m and n:
            if nums1[0] <= nums2[0]:
                r.append(nums1.pop(0))
                m -= 1
            else:
                r.append(nums2.pop(0))
                n -= 1
        if m:
            r.extend(nums1)
        if n:
            r.extend(nums2)
        nums1 = r
        print(nums1)


sol = Solution()
sol.merge([1, 3, 5], 3, [2, 4, 6, 8], 4)
sol.merge([1], 1, [], 0)
sol.merge([0], 0, [1], 1)
