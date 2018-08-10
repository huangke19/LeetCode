# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSame(root.left, root.right)

    def isSame(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.isSame(p.right, q.left) and self.isSame(p.left, q.right)
        return False
