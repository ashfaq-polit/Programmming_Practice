#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

def permutations(nums):
    res = []
    if len(nums) == 1:
        return [nums.copy()]
    
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permutations(nums)
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res

def permutations_backtrack(nums):
    res = []
        
    def permute(nums, l, r):
        if l == r:
            res.append(nums.copy())
            return
          
        for i in range(l, r):
            nums[l], nums[i] = nums[i], nums[l]
            permute(nums, l+1, r)
            nums[l], nums[i] = nums[i], nums[l]
            
    permute(nums, 0, len(nums))
    return res
  
       
nums = [1,2,3]
permutations_backtrack(nums)        
        
    