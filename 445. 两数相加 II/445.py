# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        t1 = []
        while l1:
            t1.append(l1.val)
            l1 = l1.next

        t2 = []
        while l2:
            t2.append(l2.val)
            l2 = l2.next

        num1 = int(''.join([str(i) for i in t1]))
        num2 = int(''.join([str(i) for i in t2]))
        num = num1 + num2
        newt = [int(i) for i in str(num)]

        res = tmp = ListNode(1)
        for i in newt:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return res.next

