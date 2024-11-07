#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""
import numpy as np
nums = [1, 12, -5, -6, 50, 3]
k=4
maxm = -9999
start = 0
sum1 = 0
end = 0

for end in range(len(nums)):
    sum1 = sum1 + nums[end]
    #print(sum1/k)
    #print(start)
    #print(end)
    if (end - start + 1) == k:
        maxm = np.maximum(maxm, sum1/k)
        #print(maxm)
        sum1 = sum1 - nums[start]
        start = start + 1
        
           
print('Maximum avg:', maxm)
    
    