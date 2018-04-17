#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        max_value = -10000000000
        tmp = 0
        for i in range(length):
            tmp = max(tmp + nums[i], nums[i])
            max_value = max(max_value, tmp)
        return max_value


sol = Solution()
assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert sol.maxSubArray([-2, 1, -3]) == 1
assert sol.maxSubArray([-3]) == -3
assert sol.maxSubArray([-3, -2, -1]) == -1
