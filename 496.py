#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 新建一个栈用于存储输出
# 遍历numbers1
# 找出numbers2中i的index
# 在numbers2中从index开始找，第一个数就是，如果没有则是-1


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums1:
            k = -1
            start = nums2.index(i)
            for y in nums2[start:]:
                if y > i:
                    k = y
                    break
            result.append(k)
        return result


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

if __name__ == '__main__':
    solution = Solution()
    t = solution.nextGreaterElement(nums1, nums2)
    print(t)
