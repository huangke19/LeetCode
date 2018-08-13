# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        t = []
        while head:
            t.append(head.val)
            head = head.next

        t.sort()

        res = tmp = ListNode(1)
        for i in t:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return res.next