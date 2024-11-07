#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

height = [1,8,6,2,5,4,8,3,7]
max_area  = 0

for i in range(len(height)-1):
    for j in range(i+1,len(height)):
        area = min(height[i], height[j]) * (j-i)
        if area > max_area:
            max_area = area 
            
########O(n) solution
height = [1,8,6,2,5,4,8,3,7]

l = 0
r = len(height) - 1
area = 0

while l < r:
    area = max(area, (r - l) * min(height[l], height[r]))
    if height[l] <= height[r]:
        l += 1
    else:
        r -= 1
        
print(area)  