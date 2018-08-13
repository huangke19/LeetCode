# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t1 = []
        t2 = []
        while l1:
            t1.append(l1.val)
            l1 = l1.next
        while l2:
            t2.append(l2.val)
            l2 = l2.next
        t3 = t1 + t2
        t3.sort()
        res = tmp = ListNode(1)
        for i in t3:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return res.next


