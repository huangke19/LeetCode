# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None

        t = []
        while head:
            t.append(head.val)
            head = head.next

        st = []
        lt = []
        s = set()
        for i in t:
            if i < x:
                st.append(i)
            else:
                lt.append(i)
        newt = st + lt

        res = tmp = ListNode(1)
        for i in newt:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return res.next