#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        try:
            s = int(re.match('\s*\+?-?\d+', str).group())
            if not -2 ** 31 < s < 2 ** 31 - 1:
                s = -2147483648 if s < 0 else 2147483647
        except AttributeError:
            s = 0
        except ValueError:
            s = 0
        return s
