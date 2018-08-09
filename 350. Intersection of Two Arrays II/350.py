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

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # from collections import Counter
        # c1 = Counter(nums1)
        # c2 = Counter(nums2)
        # return list((c1 & c2))
        l1 = len(nums1)
        l2 = len(nums2)
        min_nums = nums1 if l1 <= l2 else nums2
        max_nums = nums2 if l1 <= l2 else nums1
        # s2 = set(max_nums)
        res = []
        for i in min_nums:
            if i in max_nums:
                res.append(i)
                max_nums.remove(i)
        return res

sol = Solution()
# assert sol.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
print(sol.intersect([1, 2, 2, 1], [2, 2]))
