#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

nums = [-1,0,3,5,9,12]
target = 9

def Binary_Search(nums, target):
    left = 0
    mid = len(nums) // 2
    right = len(nums) - 1
    
    while left <= right:
        mid = (right + left) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid
    return -1


Binary_Search(nums, target)
    
    
#########First bad version
n = 5
bad = 4

def isBadVersion(n):
    if n < bad:
        return False
    return True

def firstBadVersion(n, bad):
    left = 0
    right = n-1
    if n <2:
        return n
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid) and isBadVersion(mid-1) == False:
            return mid
        elif isBadVersion(mid-1):
            right = mid - 1
        else:
            left = mid + 1
            
firstBadVersion(n, bad)
        
    
##########Search in Rotated Sorted Array    
nums = [4,5,6,7,0,1,2]
target = 3

def search_sorted_array(nums,target):
    left = 0
    right = len(nums)-1
    
            
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        if nums[left] <= nums[mid]:
            if target < nums[left] or target > nums[mid]:
                left = mid + 1
            else:
                right = mid -1
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid -1
            else:
                left = mid + 1
    return -1
                

search_sorted_array(nums, target)             
            
        
            
        
        




















    
        