#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""
#Inspired from https://www.youtube.com/watch?v=dJ7sWiOoK7g
nums = [2,3,0,4,1,1,2,3,2]
count = 0
l, r = 0, 0

while r < len(nums)-1:    
    farthest = 0
    for i in range(l, r+1):
        farthest = max(farthest, i + nums[i])
    l = r + 1
    r = farthest
    count += 1
    
print(count)    
        
    
