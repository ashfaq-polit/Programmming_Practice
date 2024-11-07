#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

nums = [2,3,-2,-4]
maxm = float('-inf')

####Brute force
for i in range(len(nums)):
    total = nums[i]
    for j in range(i+1, len(nums)):
        total *= nums[j]
        if total > maxm:
            maxm = total
print('Maximum:', maxm)



###Maximum product subarray 
nums = [2,3,-2,-4]

def maxm_prod_subarray(nums): 
    n = len(nums)
    left_prod, right_prod = 1, 1
    maxm = 0
    
    for i in range(n):
        left_prod *= nums[i] 
        right_prod *= nums[n-i-1]
        maxm = max(left_prod, right_prod, maxm)
            
    return maxm
            
        
maxm_prod_subarray(nums) 



arr = [2,3,0,4,7]
# [2,3,9,3,9]


def max_product(arr):
    max1, k = 0, 0
    for i in range(len(arr)):
        if arr[i] > max1:
            max1 = arr[i]
            k = i
            
            
    max_2nd = 0
    for i in range(len(arr)):
        if arr[i] > max_2nd and i != k:
            max_2nd = arr[i]
            
    return max1 * max_2nd


max_product(arr)