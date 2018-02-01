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
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n:
            return None
        # 1 分别取出每一位数，加入列表
        l = []
        s = set()
        while n != 1:
            while n:
                l.append(n % 10)
                n = n // 10
            # 2 每一位数取平方相加，生成新数
            n = sum([x * x for x in l])
            l.clear()
            # when to end ?
            if not n in s:
                s.add(n)
            else:
                return False
        return True


sol = Solution()
assert sol.isHappy(191) == False
assert sol.isHappy(82) == True
assert sol.isHappy(68) == True
assert sol.isHappy(100) == True

print('tests pass')
