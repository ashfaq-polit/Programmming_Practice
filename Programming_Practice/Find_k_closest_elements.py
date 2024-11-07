#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""
#https://www.youtube.com/watch?v=o-YDQzHoaKM
#Need to be improved

def k_closest_int(arr, k, x):
    left = 0
    right = len(arr)-k
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] - x < x - arr[mid+k]:
            left = mid + 1
        else:
            right = mid
    return arr[left:left+k]
        
            

arr = [1,2,3,4,5,6,7,8,9,10]
k = 4 #k closest integers
x = 7 #value in the array

k_closest_int(arr, k, x)
        
        