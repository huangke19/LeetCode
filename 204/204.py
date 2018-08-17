#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1. 检查先决条件
2. 定义子程序要解决的问题
3. 为子程序命名
4. 决定如何测试子程序
5. 在标准库中搜寻可用的功能
6. 考虑错误处理
7. 考虑效率问题
8. 研究算法和数据类型
9. 编写伪代码
    1. 首先简要地用一句话来写下该子程序的目的，
    2. 编写很高层次的伪代码
    3. 考虑数据
    4. 检查伪代码
10. 在伪代码中试验一些想法，留下最好的想法
'''


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        s = [True] * n
        s[0] = s[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == True:
                s[i * i:n:i] = [False] * len(s[i * i:n:i])
        return sum(s)


sol = Solution()
print(sol.countPrimes(10))
print(sol.countPrimes(499979))
# print(sol.is_prime(7))
