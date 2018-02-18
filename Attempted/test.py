#!/usr/bin/env python
# -*- coding: utf-8 -*-

def countPrimes1(n):
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


def countPrimes2(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return 0
    s = [1] * n
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i] == 1:
            s[i * i:n:i] = [0] * len(s[i * i:n:i])
    return sum(s)


def countPrimes3(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return 0
    s = [1] * n
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i] == 1:
            s[i * i:n:i] = [0] * len(s[i * i:n:i])
    return sum(s)


def countPrimes4(n):
    """
    :type n: int
    :rtype: int
    """
    from array import array
    if n < 2:
        return 0
    s = array('i', [1] * n)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i] == 1:
            s[i * i:n:i] = array('i', [0]) * len(s[i * i:n:i])
    return sum(s)


print(countPrimes1(1000000))
print(countPrimes2(1000000))
print(countPrimes3(1000000))
print(countPrimes4(1000000))
#
# import cProfile
#
# cProfile.run("countPrimes1(10000000)")
# cProfile.run("countPrimes2(10000000)")
# cProfile.run("countPrimes3(10000000)")
# cProfile.run("countPrimes4(10000000)")
