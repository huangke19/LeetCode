# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        if not head.next:
            return head

        t = []
        while head:
            t.append(head.val)
            head = head.next

        n = len(t)
        if n % 2 != 0:
            tmpt = [x for x in range(n - 1) if x % 2 == 0]
        else:
            tmpt = [x for x in range(n) if x % 2 == 0]

        for i in tmpt:
            t[i], t[i + 1] = t[i + 1], t[i]
        res = tmp = ListNode(1)

        for i in t:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return res.next
