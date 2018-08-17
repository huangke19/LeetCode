# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        t = []
        while head:
            t.append(head.val)
            head = head.next

        n = len(t) // k
        for i in range(n):
            t[i * k:i * k + k] = t[i * k:i * k + k][::-1]

        res = tmp = ListNode(1)
        for i in t:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return res.next