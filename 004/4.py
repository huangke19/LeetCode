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


class Solution1:
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

class Solution2:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 合并两个数组
        nums3 = sorted(nums1 + nums2)
        # 新数组排序
        n = len(nums3)
        # 判断如果为偶数，取中间两位
        if n % 2 == 0:
            index1, index2 = int(n / 2 - 1), int(n / 2)
            mid_num = (nums3[index1] + nums3[index2]) / 2
        # 如果为奇数，取中间一位
        else:
            index = int((n - 1) / 2)
            mid_num = nums3[index]
        # 取中位数
        print(mid_num)
        return mid_num


nums1 = [1]
nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

s = Solution()
s.findMedianSortedArrays(nums1, nums2)
