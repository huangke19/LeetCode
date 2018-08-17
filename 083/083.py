# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def deleteDuplicates(self, head):
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

        newt = []
        s = set()
        for i in t:
            if not i in s:
                s.add(i)
                newt.append(i)
            else:
                continue

        res = tmp = ListNode(1)
        for i in newt:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return res.next