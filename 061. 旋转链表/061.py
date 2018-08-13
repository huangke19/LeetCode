# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        t = []
        while head:
            t.append(head.val)
            head = head.next

        newt = []
        k = k % len(t)
        for i in range(k):
            newt = [t.pop()] + newt
        newt = newt + t

        res = tmp = ListNode(1)
        for i in newt:
            tmp.next = ListNode(i)
            tmp = tmp.next
        # return res.next
