#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        return Counter(s) == Counter(t)


sol = Solution()
assert sol.isAnagram("anagram", "nagaram") == True
assert sol.isAnagram("rat", "car") == False
