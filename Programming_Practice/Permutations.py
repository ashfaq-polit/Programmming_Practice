#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

def backtrack(nums, res, subset):
    if len(subset) == len(nums):
        res.append(subset.copy())
         

    for i in range(0, len(nums)):  
       if nums[i] in subset:
            continue;

       subset.append(nums[i])
       backtrack(nums, res, subset)
       subset.pop()

   



def Permutations(nums):
    nums.sort()
    res = []
    subset = []
    index = 0
    backtrack(nums, res, subset)
    return res


nums = [1,3,2]
Permutations(nums)