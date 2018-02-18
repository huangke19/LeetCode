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
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # 新建一个中转栈和一个新数组
        # 中转栈比较，如果
        mid = [0]
        new = []
        cou = []
        newchars = []
        while chars:
            if chars[-1] != mid[-1]:
                new.append(chars.pop())
                cou.append(1)
                mid[-1] = new[-1]
            else:
                cou[-1] += 1
                chars.pop()
        while new and cou:
            newchars.append(new.pop())
            if cou[-1] == 1:
                cou.pop()
                continue
            else:
                if len(str(cou[-1])) > 1:
                    for i in str(cou[-1]):
                        newchars.append(i)
                else:
                    newchars.append(str(cou[-1]))
                cou.pop()
        chars = newchars
        return len(chars)


sol = Solution()
print(sol.compress(["a", "a", "b", "b", "c", "c", "c"]))
# print(sol.compress(["a"]))
# print(sol.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
