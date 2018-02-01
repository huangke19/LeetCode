#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
          """
        # 1. if not nums: return 0
        if not nums:
            return 0
        # 2. 需要一个变量longest来表示最大长度 max(exists, new)
        longest = 1
        # 3. max, deque
        q = []
        # 1st num enque
        for num in nums:
            if not q:
                q.append(num)
            # compare next to 1st
            # if next > q.top, enque, longest+1
            elif num > q[-1]:
                q.append(num)
                longest = max(longest, len(q))
            # if next <= q.top, q.deque all , longest = max(longest,len(q))
            else:
                longest = max(longest, len(q))
                q.clear()
                q.append(num)
        return longest


sol = Solution()
assert sol.findLengthOfLCIS([1, 3, 5, 4, 7]) == 3
assert sol.findLengthOfLCIS([2, 2, 2, 2, 2]) == 1
assert sol.findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4]) == 3
assert sol.findLengthOfLCIS([]) == 0
