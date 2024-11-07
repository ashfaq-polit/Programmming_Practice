#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

nums = [3,2,3,1,2,4,5,5,6]
k = 4
k = len(nums) - k

def quickSelect(l,r):
    p, pivot = l, nums[r]
    for i in range(l, r):
        # print(i, r)

        if nums[i] < pivot:
            nums[p], nums[i] = nums[i], nums[p]
            p += 1
    nums[p], nums[r] = nums[r], nums[p]
    if p < k:
        return quickSelect(p+1, r)
    elif p > k:
        return quickSelect(l, p-1)
    else:
        return nums[p]
            
quickSelect(0, len(nums) - 1)
            
    