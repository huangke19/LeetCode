# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        t = []
        while head:
            t.append(head.val)
            head = head.next
        return t == t[::-1]