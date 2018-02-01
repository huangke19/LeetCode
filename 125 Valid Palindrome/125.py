#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return s == s[::-1]


sol = Solution()

ss1 = "0b"
print(sol.isPalindrome(ss1))
