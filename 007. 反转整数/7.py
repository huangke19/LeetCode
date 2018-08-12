class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = -1 if x < 0 else 1
        rx = f * int(str(abs(x))[::-1])
        return rx if -(2**31-1)< rx <2**31 else 0