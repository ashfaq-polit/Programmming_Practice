#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

def Combination_sum(candidates, target):
   res  = []      
   def backtrack(i, cur, total):
       if total == target:
           res.append(cur.copy())
           return
       if i >= len(candidates) or total > target:
           return
       cur.append(candidates[i])
       backtrack(i, cur, total + candidates[i])
       cur.pop()
       backtrack(i+1, cur, total)

   backtrack(0, [], 0)
   return res



def backtrack(nums, target, res, subset, index):
    if target == 0:
        res.append(subset.copy())
    for i in range(index, len(nums)):
            subset.append(nums[i])
            newtarget = target - nums[i]
            if newtarget >= 0:
                backtrack(nums, newtarget, res, subset, i)
            subset.pop()


def Combination_sum(nums, target):
    nums.sort()
    res = []
    subset = []
    index = 0
    backtrack(nums, target, res, subset, index)
    return res
    
    
    
candidates = [2,3,6,7]
target = 7
Combination_sum(candidates, target)