#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

nums = [3,2,3]

count = []
unique = []

for i in nums:
    if i not in unique:
        unique.append(i)
        
#print(unique)
count = [0] * len(unique)

for i in range(len(nums)):
    for j in range(len(unique)):
        if unique[j] == nums[i]:
            count[j] += 1
            if count[j] > len(nums)/2:
                print(unique[j])
            
#print(count)

#########Moore's voting algorithm
nums = [2,2,1,1,1,1,1]
res = nums[0]
count = 0

for i in nums:
    if count == 0:
        res = i
    if i == res:
        count += 1
    else:
        count -= 1

  

###Hash-map solution
nums = [2,2,1,1,1,1,1]
count = {}
res, maxm = 0, 0

for i in nums:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
    res = i if count[i] > maxm else res
    maxm = max(maxm, count[i])
    
        

    
    
        


    

        