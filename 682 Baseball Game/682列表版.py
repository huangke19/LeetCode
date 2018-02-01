#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        t = [0, 0]
        for op in ops:
            if op == '+':
                t.append(t[-1] + t[-2])
            if op == 'D':
                t.append(t[-1] * 2)
            if op == 'C':
                t.pop()
            else:
                t.append(int(op))
        return sum(t)

if __name__ == '__main__':
    s = Solution()
    print(s.calPoints(["+"]))
    print(s.calPoints(["5", "2", "C", "D", "+"]))
    print(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))