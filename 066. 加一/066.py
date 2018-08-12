class Solution:

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s_digits = (str(i) for i in digits)
        num = int(''.join(s_digits))
        out_num = num + 1

        return [int(i) for i in str(out_num)]
