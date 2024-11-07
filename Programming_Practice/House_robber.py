#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

def house_robber(nums):
    dp = [0] * len(nums)
    
    dp[0] = nums[0]
    dp[1] = max(nums[1], nums[0])
    
    for i in range(2, len(nums)):
        dp[i] = nums[i] + dp[i-2]
        maxm = max(dp[i-1], dp[i])
    return maxm
    
nums = [2,1,3,4]
house_robber(nums)