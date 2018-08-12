class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict(
            I=1,
            V=5,
            X=10,
            L=50,
            C=100,
            D=500,
            M=1000,
            XL=40,
            XC=90,
            CD=400,
            CM=900,
            IV=4,
            IX=9,
        )

        i = 0
        res = 0
        while i < len(s):
            if s[i:i + 2] in d:
                res += d.get(s[i:i + 2])
                i += 2
            else:
                res += d.get(s[i])
                i += 1

        return res