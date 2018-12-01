#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ln1, ln2 = '', ''
        while l1:
            ln1 += str(l1.val)
            l1 = l1.next
        while l2:
            ln2 += str(l2.val)
            l2 = l2.next

        # 将两个整数相加

        ln3 = int(ln1[::-1]) + int(ln2[::-1])
        ln3 = [int(x) for x in list(str(ln3)[::-1])]

        # 将和用链表的形式表示

        d = {}
        for i, v in enumerate(ln3):
            d[i] = ListNode(v)
        for i in range(len(ln3) - 1):
            d[i].next = d[i + 1]

        return d[0]


class Solution2:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 将两个链表的数取出来，转化为数字形式
        # 将链表转化为列表
        list1, list2 = [], []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        # 列表翻转
        list1.reverse()
        list2.reverse()

        # 将列表转化为字符串
        list1 = [str(i) for i in list1]
        list2 = [str(i) for i in list2]
        str1 = ''.join(list1)
        str2 = ''.join(list2)

        # 将字符串转化为数字
        num1, num2 = int(str1), int(str2)

        # 将得到的两个数进行计算
        num3 = num1 + num2

        # 将结果反转并恢复成链表的形式

        # 结果恢复成可迭代的字符并反转
        str3 = str(num3)[::-1]

        # 生成头部节点
        head = curnode = ListNode(0)

        # 遍历字符串
        for i in str3:
            # 每个cur转为数字后单独成一个结点
            node = ListNode(int(i))
            # 将各个结点串起来
            curnode.next = node
            curnode = curnode.next

        # 去掉头部返回
        return head.next


''' 节点拼接有不同的方法，解法1和解法2分别展示了两种不同的拼接方法 '''
