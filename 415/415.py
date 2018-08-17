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


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s1 = s2 = 0
        for i, v in enumerate(num1):
            s1 += int(v) * (10 ** (len(num1) - i - 1))
        for i, v in enumerate(num2):
            s2 += int(v) * (10 ** (len(num2) - i - 1))
        s = s1 + s2
        
        return str(s)


if __name__ == '__main__':
    solution = Solution()
    print
    solution.addStrings('111', '222')
