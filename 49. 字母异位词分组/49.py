import copy

class Solution:

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        while strs:
            tmp = []
            n = len(strs)
            for i in range(n):
                if self.isanagrams(strs[0], strs[i]):
                    tmp.append(strs[i])
            res.append(tmp)
            for t in tmp:
                strs.remove(t)
        return res

    def isanagrams(self, a, b):
        al = sorted(list(a))
        bl = sorted(list(b))
        return al == bl

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

sol = Solution()
sol.groupAnagrams(strs)

sol.isanagrams('eat', 'tan')
