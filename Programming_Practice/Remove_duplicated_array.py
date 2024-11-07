#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

nums = [0,0,1,1,1,2,2,3,3,4]

l, r = 0, 1
count = 1

for r in range(1, len(nums)):
    if nums[l] != nums[r]:
        count += 1
        l += 1
        nums[l] = nums[r]
        
print(nums[:count])
print('Count:', count) 



####Remove element
nums = [0,1,2,2,3,0,4,2]
val = 2

l, r = 0, 0
count = 0

for r in range(len(nums)):
    if nums[r] != val:
        nums[l] = nums[r]
        l += 1
        
print('Count:', l)

    
        