#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

nums = [1,1,1,2,2,3]
k = 2

def Top_k_frequent(nums, k):
    count = {}
    
    for i in nums:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
            
    freq = [[] for i in range(len(nums)+1)]
    
    for key, val in count.items():
        freq[val].append(key)
        
    res = []
    
    for i in range(len(freq)-1,0,-1):
        for j in freq[i]:
            res.append(j)
            print(len(res))
            if len(res) == k:
                return res
    
Top_k_frequent(nums, k)