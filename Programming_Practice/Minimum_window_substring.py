#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""
###########Unsolved
s = "ADOBECODEBANC" 
t = "ABC"

window_hash, t_hash = {}, {}

for i in t:
    if i not in t_hash:
        t_hash[i] = 1
    else:
        t_hash[i] += 1
        
need, have = len(t), 0
result, res_len = [], -9999

left = 0
for right in range(9):
    if s[right] in t:
        if s[right] not in window_hash:
            window_hash[s[right]] = 1
        else:
            window_hash[s[right]] += 1
            print(have, right)
    if have == need:
        count = 0
        for key in window_hash:
            if window_hash[key] >= t_hash[key]:
                count += 1
                have += 1
        if count == len(t_hash):
            result.append(s[left:right+1])
            print(result)            
            window_hash[s[left]] -= 1
            if window_hash[s[left]] == 0:
                window_hash.pop(s[left])
            left += 1
            have -= 1

    print(right)    
        
