class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        from itertools import combinations

        s = list(range(1, n + 1))
        return list(combinations(s, k))