#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # from collections import Counter
        # return Counter(s) == Counter(t)

        sl = sorted(list(s))
        tl = sorted(list(t))

        print(sl, tl)
        return sl == tl

sol = Solution()

sol.isAnagram('t', 'a')
# assert sol.isAnagram("anagram", "nagaram") == True
# assert sol.isAnagram("rat", "car") == False
