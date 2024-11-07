#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""
import numpy as np
nums = [2,3,1,2,4,3]
target = 7

l = 0
size = 9999
total = 0

for r in range(len(nums)):
    total += nums[r]
    if total >= target:
        while total >= target:
            size = np.minimum(size, r - l + 1)
            print('size:',size)
            print(total)
            total -= nums[l]
            l += 1
            
if size == 9999:
    size = 0
print('Minimum size:', size)       
        
        
    