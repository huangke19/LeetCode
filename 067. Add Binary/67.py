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
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '0' and b == '0':
            return '0'
        else:
            length_a = len(a)
            length_b = len(b)
            a_ = 0
            b_ = 0
            
            for n1, a1 in enumerate(a):
                s = int(a1) * (2 ** (length_a - n1 - 1))
                a_ += s
            for n1, b1 in enumerate(b):
                s = int(b1) * (2 ** (length_b - n1 - 1))
                b_ += s
            sum_ab = a_ + b_
            return str(bin(sum_ab))[2:]


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('0', '0'))
