#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Stack.ArrayStack import ArrayStack


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {"}": "{", "]": "[", ")": "("}
        t = ArrayStack()
        if not s:
            return True
        for i in s:
            if t.isEmpty():
                t.push(i)
                continue
            if i in '([{':
                t.push(i)
            else:
                if d[i] != t.top():
                    t.push(i)
                else:
                    t.pop()
        return t.isEmpty()


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()[]{}"))
    print(solution.isValid("()[{}"))
    print(solution.isValid("(())[]{}"))
    print(solution.isValid("(])"))
    print(solution.isValid(""))
