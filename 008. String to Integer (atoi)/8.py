class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        
        _max = 2147483647
        _min = -2147483648
        
        s = re.match('\s*[-\+]?\d+', str)
        if s:
            s = int(s.group())
            if s > _max: s = _max
            if s < _min: s = _min
            return s
        return 0
