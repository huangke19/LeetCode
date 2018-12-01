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


# O(n**2)
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return x, y


# O(n)
class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 定义一个容器装已经迭代的数
        looped_dict = dict()
        # 带索引迭代数组
        for i, v in enumerate(nums):
            # 迭代到每个数时，都检查(target-当前数)是否已经在容器里
            sub = target - v
            if sub in looped_dict:
                # 如果在，则算找到两个数
                # 找到两个数了，还需要找到他们的索引
                # 当前数的索引通过enumerate获得
                index2 = i
                # (target-当前数)的索引需要使用一种方法保存
                # list可以，但检查耗时，set()存放数的话不能保存索引
                # 使用dict()可以兼顾效率并保存索引
                index1 = looped_dict[sub]
                # 返回两个值的索引
                return index1, index2
            # 为了检查方便，需要将{key:value}反转为{value:key}
            else:
                cur_dict = {v: i}
                # 如果不在，将{value:key}放入容器以备后续检查
                looped_dict.update(cur_dict)
        # 如果循环完了都没找到，返回None
        return None
