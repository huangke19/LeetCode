#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # import re
        # s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        # return s == s[::-1]
        l = []
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        for i in range(len(l)):
            if l[i] != l[-(i + 1)]:
                return False
        return True

sol = Solution()

ss1 = "0P"
print(sol.isPalindrome(ss1))
