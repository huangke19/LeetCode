#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        

        """
        if x in [0, 1]:
            return x
        limit = 0.001
        low = 0
        up = x
        y = x / 2
        while abs(y ** 2 - x) > limit:
            if y ** 2 > x:
                up = y
                y = up - (up - low) / 2
            if y ** 2 < x:
                low = y
                y = low + (up - low) / 2
        return int(y)


sol = Solution()
sol.mySqrt(87)
assert sol.mySqrt(0) == 0
assert sol.mySqrt(4) == 2
assert sol.mySqrt(1) == 1
assert sol.mySqrt(8) == 2
assert sol.mySqrt(10) == 3
assert sol.mySqrt(18) == 4
assert sol.mySqrt(28) == 5
assert sol.mySqrt(58) == 7
assert sol.mySqrt(29) == 5
assert sol.mySqrt(80) == 8
print("tests pass, congratulations!")
