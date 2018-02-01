#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Stack.ArrayStack import ArrayStack


class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        self.mystack = ArrayStack()
        self.mystack.push(0)
        self.mystack.push(0)
        for op in ops:
            if op not in {'+', 'C', 'D'}:
                self.mystack.push(op)
            elif op == '+':
                a = self.mystack.pop()
                b = self.mystack.pop()
                c = int(a) + int(b)
                self.mystack.push(b)
                self.mystack.push(a)
                self.mystack.push(c)
            elif op == 'D':
                d = self.mystack.top()
                self.mystack.push(d)
                self.mystack.push(int(d) * 2)
            elif op == 'C':
                self.mystack.pop()
        total = 0
        while not self.mystack.isEmpty():
            total += int(self.mystack.pop())
        
        return total


if __name__ == '__main__':
    s = Solution()
    print(s.calPoints(["+"]))
    print(s.calPoints(["5", "2", "C", "D", "+"]))
    print(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
