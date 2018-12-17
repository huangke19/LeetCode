class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = -1 if x < 0 else 1
        rx = f * int(str(abs(x))[::-1])
        return rx if -(2 ** 31 - 1) < rx < 2 ** 31 else 0


class Solution2:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 记录符号，去掉符号
        flag = -1 if x < 0 else 1
        newx = str(abs(x))
        # 反转数字
        newx = int(newx[::-1])
        # 检查范围
        if not -(2 ** 31) < newx < 2 ** 31:
            return 0
        else:
            res = flag * newx
            return res


x1 = 123
x2 = -123
x3 = 1534236469

s = Solution2()
res1 = s.reverse(x1)
res2 = s.reverse(x2)
res3 = s.reverse(x3)

print(res1, res2)
print(res3)
