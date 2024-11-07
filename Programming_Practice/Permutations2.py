#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

def backtrack(hash_map, res, subset):
    if len(subset) == len(nums):
        res.append(subset.copy())
         

    for i in hash_map:  
       if (hash_map[i] > 0):
           subset.append(i)
           hash_map[i] -= 1
           backtrack(hash_map, res, subset)
           subset.pop()
           hash_map[i] += 1


def Permutations2(nums):
    from collections import Counter

    nums.sort()
    res = []
    subset = []

    hash_map = Counter(nums)
       
    backtrack(hash_map, res, subset)
    return res


nums = [1,1,2]
Permutations2(nums)