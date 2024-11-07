#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

array = [-1,0,1,2,-1,-4]
#array = [-5, 2, 1 ,3, 4]
array = sorted(array)
list = []
length = len(array)

for i in range(len(array)):
    if i > 0 and array[i] == array[i-1]:
        continue
    else:
        l = i + 1
        r = length - 1
        while l < r:
            if array[l] + array[r] + array[i] < 0:
                l = l + 1
            elif array[l] + array[r] + array[i]> 0:
                r = r - 1
            else:
                list.append([array[i], array[l], array[r]])
                l += 1
                r -= 1



  
        