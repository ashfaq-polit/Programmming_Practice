#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

g = [1,2]
s = [1,2,3]

g = sorted(g)
s = sorted(s)

left, right = 0, 0

while left < len(g) and right < len(s):
    if s[right] >= g[left]:
        left += 1
        right += 1
    else:
       right += 1 
        
print('Count:', left)