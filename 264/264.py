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
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        from queue import deque
        a2 = deque()
        a3 = deque()
        a5 = deque()
        a2.append(2)
        a3.append(3)
        a5.append(5)
        x = 1
        while n > 1:
            x2 = a2.popleft()
            x3 = a3.popleft()
            x5 = a5.popleft()
            x = min(x2, x3, x5)
            if x == x2:
                a3.appendleft(x3)
                a5.appendleft(x5)
                a2.append(x * 2)
                a3.append(x * 3)
                a5.append(x * 5)
            elif x == x3:
                a2.appendleft(x2)
                a5.appendleft(x5)
                a3.append(x * 3)
                a5.append(x * 5)
            elif x == x5:
                a2.appendleft(x2)
                a3.appendleft(x3)
                a5.append(x * 5)
            n -= 1
        return x


sol = Solution()
print(sol.nthUglyNumber(1))
print(sol.nthUglyNumber(2))
print(sol.nthUglyNumber(3))
print(sol.nthUglyNumber(4))
print(sol.nthUglyNumber(5))
print(sol.nthUglyNumber(6))
print(sol.nthUglyNumber(7))
print(sol.nthUglyNumber(8))
print(sol.nthUglyNumber(9))
print(sol.nthUglyNumber(10))


