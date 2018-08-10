class Solution:

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        num = 0
        for i in range(0, len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if (sub == sub[::-1]):
                    num = num + 1
        print(num)
        return num

    def isPal(self, a):
        return a == a[::-1]

s = "xkjkqlajprjwefilxgpdpebieswu"
# s = 'abc'
sol = Solution()
sol.countSubstrings(s)
