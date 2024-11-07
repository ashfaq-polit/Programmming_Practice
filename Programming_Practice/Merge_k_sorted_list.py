#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

# l1 = [1,4,5]
# l2 = [1,3,4]


def merged_list(l1, l2):  
    merged = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    if i < len(l1):
        merged.append(l1[i])
    if j < len(l2):
        merged.append(l2[j])
    return merged

#merged_list(l1, l2)
 
lists = [[1,4,5],[1,3,4],[2,6]]
#lists = []     
      
def merged_k_lists(lists):
    if not lists:
        return []
    else:
        res = lists[0]
        for i in range(1, len(lists)):
            res = merged_list(res, lists[i])
            # res.append(merged)
        return res
        
merged_k_lists(lists)    