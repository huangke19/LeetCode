# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        t1 = []
        while headA:
            t1.append(headA)
            headA = headA.next

        t2 = []
        while headB:
            t2.append(headB)
            headB = headB.next

        t1 = t1[::-1]
        t2 = t2[::-1]

        res = []
        n = min(len(t1), len(t2))
        for i in range(n):
            if t1[i] == t2[i]:
                res.append(t1[i])
            else:
                break

        if not res:
            return None
        return res.pop()



