#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

nums =  [-2,1,-3,4,-1,2,1,-5,4]
maxm = float('-inf')

####Brute force/Dynamic programming
def maximum_subarray(nums):
    dp = [0] * len(nums)
    maxm = 0
    for i in range(len(nums)):
        dp[i] = nums[i]
        for j in range(i+1, len(nums)):
            dp[j] = dp[j-1] + nums[j]
            if dp[j] > maxm:
                maxm = dp[j]
    return maxm


###Using two pointers
l, r = 0, 0
total = 0

for r in range(l, len(nums)):
    total += nums[r]
    if total < 0:
        l = r + 1
        total = 0
    if total > maxm:
        maxm = total
        
###Using one pointer            
total = 0            
for i in nums:
    total += i
    if total < 0:
        total = 0
    if total > maxm:
        maxm = total
    
