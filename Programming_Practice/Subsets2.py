#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""


def backtrack(nums, res, subset, index):
        if subset not in res:
            res.append(subset.copy())

            for i in range(index, len(nums)):  
                    subset.append(nums[i])
                    backtrack(nums, res, subset, i+1)
                    subset.pop()
        else:
            res = res.copy()
            
def backtrack(nums, res, subset, index):
            res.append(subset.copy())

            for i in range(index, len(nums)):  
                if i > index and nums[i] == nums[i-1]:
                    continue
                else:
                    subset.append(nums[i])
                    backtrack(nums, res, subset, i+1)
                    subset.pop()


def subsets2(nums):
    nums.sort()
    res = []
    subset = []
    index = 0
    backtrack(nums, res, subset, index)
    return res


nums = [1,2,2]
subsets2(nums)