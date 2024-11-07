#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

def longest_inc_subseq(nums):
    dp = [1] * len(nums)
    
    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)



###https://www.youtube.com/watch?v=Xq3hlMvhrkE
import numpy as np

def longest_incr_subseq(nums):
     n = len(nums)
     LIS = [1] * n
     i , j, maxm  = 1, 1, 1
     for i in range(n-1):
         for j in range(i):
             if nums[i]> nums[j] and LIS[i] <= LIS[j]:
                 LIS[i] = LIS[j] + 1
                 if LIS[i] > maxm:
                     maxm = LIS[i]
             else:
                 continue
     return np.max(LIS)

nums = [10,9,2,5,3,7,101,18]
longest_incr_subseq(nums)