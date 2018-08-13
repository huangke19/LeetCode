# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        m = len(l) - n
        l = l[: m] + l[m + 1:]
        res = tmp = ListNode(1)
        for i in l:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return res.next


