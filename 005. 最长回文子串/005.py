class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'
        res = ''
        t = 0
        n = len(s)
        for i in range(0, n + 1):
            lenth = min(i + 1, n - i + 1)
            if lenth < t:
                continue
            for j in range(0, lenth):
                tmpstr = s[i - j: i + j + 1]
                if self.isPal(tmpstr):
                    res = tmpstr if len(tmpstr) >= len(res) else res
                    t = (len(res) - 1) // 2
        res = res.replace('#', '')
        print(res)
        return res

    def isPal(self, a):
        return a == a[::-1]

s = 'fuckcuf'
sol = Solution()
sol.longestPalindrome(s)
