#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
    
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.minStack or self.minStack[-1] >= x:
            self.minStack.append(x)
    
    def pop(self):
        """
        :rtype: void
        """
        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        self.stack.pop()
    
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
    
    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


t1 = time.time()

minstack = MinStack()
t2 = time.time()

minstack.push(-2)
t3 = time.time()

minstack.push(0)
t4 = time.time()
minstack.push(-3)
t5 = time.time()

# print(t1)
# print(t2 - t1)
print((t3 - t2) * 10 ** 7)
# print((t4 - t3) * 10 ** 7)
print((t5 - t4) * 10 ** 7)

# print(minstack.getMin())
# print(minstack.top())
# print(minstack.getMin())
