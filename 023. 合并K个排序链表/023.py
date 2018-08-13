# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        t1 = []
        for lis in lists:
            while lis:
                t1.append(lis.val)
                lis = lis.next
        t1.sort()
        res = tmp = ListNode(1)
        for i in t1:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return res.next
