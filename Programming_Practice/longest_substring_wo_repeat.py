#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""
import numpy as np
import collections

string = "abcabcbb"
maxm = 0
l = 0
substring = collections.defaultdict(int)

for r in range(len(string)):
    if string[r] not in substring:
        substring[string[r]] = 1
    else:
        maxm = np.maximum(maxm, r - l)
        print(maxm)
        #substring[string[r]] -= 1
        while substring[string[r]]:
            substring[string[l]] = 0
            l = l + 1
        substring[string[r]] = 1
    print(substring)         
       
        

        
        
        
    