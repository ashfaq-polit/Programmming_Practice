#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""
#Inspired from https://www.youtube.com/watch?v=yYtaV0G3mWQ

import numpy as np
import collections

trees = [1,2,3,2,2]
maxm = 0
start = 0
total = 0
collection = collections.defaultdict(int)

for r in range(len(trees)):
    collection[trees[r]] += 1
    total += 1

    
    if len(collection) > 2:
        f = trees[start]
        collection[f] -= 1
        if collection[f] == 0:
            collection.pop(f)
            
        total -= 1
        start = start + 1
        
    maxm = np.maximum(maxm, total) 
    print(collection, maxm)  
    
print(maxm)

    
    
    



