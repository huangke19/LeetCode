#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
             """
        # corner case
        words, resword, res = sorted(words), '', set()
        for word in words:
            if len(word) == 1 or word[:-1] in res:
                res.add(word)
                resword = word if resword == '' else word if len(word) > len(resword) else resword
        return resword

sol = Solution()
assert sol.longestWord(["w", "wo", "wor", "worl", "world"]) == 'world'
assert sol.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]) == 'apple'
assert sol.longestWord(
    ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]) == 'yodn'
assert sol.longestWord(
    ["b", "br", "bre", "brea", "break", "breakf", "breakfa", "breakfas", "breakfast", "l", "lu", "lun", "lunc", "lunch",
     "d", "di", "din", "dinn", "dinne", "dinner"]) == "breakfast"
