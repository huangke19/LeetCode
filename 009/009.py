class Solution:

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        sx = str(x)
        return sx == sx[::-1]
