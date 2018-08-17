#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ln1, ln2 = '', ''
        while l1:
            ln1 += str(l1.val)
            l1 = l1.next
        while l2:
            ln2 += str(l2.val)
            l2 = l2.next
        
        # 将两个整数相加
        
        ln3 = int(ln1[::-1]) + int(ln2[::-1])
        ln3 = [int(x) for x in list(str(ln3)[::-1])]
        
        # 将和用链表的形式表示
        
        d = {}
        for i, v in enumerate(ln3):
            d[i] = ListNode(v)
        for i in range(len(ln3) - 1):
            d[i].next = d[i + 1]
        
        return d[0]
