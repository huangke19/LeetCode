#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Quene_K:
    """docstring for Quene_K"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)  # 注意别忘记return
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Quene_K()
        self.q2 = Quene_K()
    
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.enqueue(x)
    
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while self.q1.size() > 1:
            self.q2.enqueue(self.q1.dequeue())
        r = self.q1.dequeue()
        while not self.q2.isEmpty():
            self.q1.enqueue(self.q2.dequeue())
        return r
    
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while self.q1.size() > 1:
            self.q2.enqueue(self.q1.dequeue())
        r = self.q1.dequeue()
        print(r)
        self.q2.enqueue(r)
        while not self.q2.isEmpty():
            self.q1.enqueue(self.q2.dequeue())
        return r
    
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q1.isEmpty()


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.top()
obj.pop()
obj.pop()
obj.pop()
print(obj.empty())
