# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None

        t = []
        while head:
            t.append(head.val)
            head = head.next

        t[m - 1:n] = t[m - 1:n][::-1]

        res = tmp = ListNode(1)
        for i in t:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return res.next
