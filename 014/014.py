class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i, g in enumerate(zip(*strs)):
            if len(set(g)) > 1:
                return strs[0][:i]
        return min(strs)

s = ["a", "a"]

sol = Solution()
print(sol.longestCommonPrefix(s))
