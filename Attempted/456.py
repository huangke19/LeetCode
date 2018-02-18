#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def find132pattern(self, nums):
        """
        find is there a 132 pattern in nums
        :type nums: List[int]
        :rtype: bool
           """
        # 1. 按顺序找3个数，后两个必须大于第1个
        # 2. 第1个最小，第2个最大，第3个居中
        import time
        
        if not nums:
            return False
        
        n = len(nums)
        # find the first num
        for i in range(n):
            stack = []
            stack.append(nums[i])
            # find another bigger one
            for j in range(i + 1, n):
                if nums[j] > stack[-1] and nums[j] > nums[i]:
                    stack.append(nums[j])
                elif nums[j] >nums[i] and nums[j] < stack[-1]:
                    return True
        return False


sol = Solution()
assert sol.find132pattern([1, 2, 3, 4]) == False
assert sol.find132pattern([3, 1, 4, 2]) == True
assert sol.find132pattern([-1, 3, 2, 0]) == True
assert sol.find132pattern([1, -4, 2, -1, 3, -3, -4, 0, -3, -1]) == True
