# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        t = []
        while head:
            t.append(head)
            head = head.next

        n = len(t)
        return t[n // 2]


