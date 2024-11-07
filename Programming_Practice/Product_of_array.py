#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

nums = [-1,1,0,-3,3]
product = [0] * len(nums)
    

for i in range(len(nums)):
    temp=1
    for j in range(len(nums)):
        if j!= i:
            temp = nums[j] * temp
        else:
            temp = temp
    product[i] = temp
    
print(product)


##########O(n) solution
nums = [-1,1,0,-3,3]

left = [0] * len(nums)
left[0] = 1
right = [0] * len(nums)
right[len(nums)-1] = 1
product = [1] * len(nums)

for i in range(1,len(nums)):
    left[i] = nums[i-1] * left[i-1]
        
for i in range(len(nums)-2,-1,-1):
    right[i] = nums[i+1] * right[i+1]
    
for i in range(len(nums)):
    product[i] = left[i] * right[i]
    
print(product)


##########O(n) solution with no extra memory use
nums = [1,2,3,4]
product = [1] * len(nums)

for i in range(1,len(nums)):
    product[i] = product[i-1] * nums[i-1]
 
temp=1
for i in range(len(nums)-1,-1,-1):
    product[i] = product[i] * temp
    temp = nums[i] * temp 
    
print(product)
    
    


    