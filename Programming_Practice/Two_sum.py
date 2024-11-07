#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

array = [3,2,4]
target = 6

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[j] + array[i] == target:
            print ([i,j])
            
        
            
#############Using Hash map
hash_map = {}

for idx, val in enumerate(array):
    rem = target - val
    if rem in hash_map:
       print([hash_map[rem], idx])
    else:
        hash_map[val] = idx
          

 
########GIven a sorted array
array = [1,3,4,5,7,11]
target = 9
length = len(array)

l = 0
r = length-1  

while l<r:
    if array[l]+ array[r] > target:
        r = r-1
    if array[l]+ array[r]< target:
        l = l+1
    if array[l]+ array[r] == target:
        print([l, r])
        break
    
########Three sum
nums = [-1,0,1,2,-1,-4]
triplet = []
for i in range(len(nums)-2):
    hash_table = {}
    target = -nums[i]
    nums_short = nums[i+1:len(nums)-1]
    for idx, val in enumerate(nums_short):
        if target - val not in nums_short:
            hash_table[idx] = val
        else:
            triplet.append([nums[i], val, target - val])
 
            
 ##Using sorted array
triplet = [] 
nums = [-1,0,1,2,-1,-4]
nums.sort()
for i in range(len(nums)-2):
    target = -nums[i]
    l = i+1
    r = len(nums)-1
    while l<r:
        if nums[l] + nums[r] == target:
            #nums[l]+ nums[r] == target:
            # print([nums[l], nums[r], nums[i]])
            triplet.append([nums[l], nums[r], nums[i]])
            l = l+1
            # r = r-1
            if nums[i] == nums[i+1]:
                l = l+1
        elif nums[l]+ nums[r] > target:
            r = r-1
        else:
            #nums[l]+ nums[r]< target:
            l = l+1


 
            

    
    
