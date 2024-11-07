#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

def Combination_sum(candidates, target):
   res  = []    
   candidates = sorted(candidates)
   def backtrack(i, cur, total):
       if total == target and cur not in res:
           res.append(cur.copy())
           return
       if i >= len(candidates) or total > target:
           return
       cur.append(candidates[i])
       backtrack(i+1, cur, total + candidates[i])
       cur.pop()
       backtrack(i+1, cur, total)
       
   backtrack(0, [], 0)
   return res

candidates = [10,1,2,7,6,1,5]
target = 8
Combination_sum(candidates, target)



def backtrack(nums, target, res, subset, index):
    if target == 0 and subset not in res:
        res.append(subset.copy())
    for i in range(index, len(nums)):
            subset.append(nums[i])
            newtarget = target - nums[i]
            if newtarget >= 0:
                backtrack(nums, newtarget, res, subset, i + 1)
            subset.pop()


def Combination_sum2(nums, target):
    nums.sort()
    res = []
    subset = []
    index = 0
    backtrack(nums, target, res, subset, index)
    return res
    
    
    
candidates = [10,1,2,7,6,1,5]
target = 8
Combination_sum2(candidates, target)