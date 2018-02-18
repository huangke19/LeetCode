#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = set(s)
        l =[]
        for i in st:
            l.append(i)
        return ''.join(sorted(l))



sol = Solution()
print(sol.removeDuplicateLetters("cbacdcbc"))