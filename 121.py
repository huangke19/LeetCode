#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
         """
        # 1. prices不为空,如果为空，返回0
        if not prices:
            return 0
        # 2. 第一个数入栈，后面的数和第一个对比，如果大于，将差存入max_profit变量，如果小于，和第一个数互换
        stack1 = []
        max_profit = 0
        for price in prices:
            if not stack1:
                stack1.append(price)
                continue
            if price >= stack1[0]:
                profit = price - stack1[0]
                max_profit = max(profit, max_profit)
            else:
                stack1[0] = price
        # 3. 重复2，完成后选出max
        return max_profit


sol = Solution()

assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
