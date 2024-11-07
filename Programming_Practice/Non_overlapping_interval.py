#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

intervals =  [[1,4],[5,6],[2,3]]
intervals = sorted(intervals)

cur_interval = intervals[0]
count = 0

for i in range(1,len(intervals)):
    if intervals[i][0] < cur_interval[1]:
        count += 1
    else:
       cur_interval[1] =  intervals[i][1]
        
print('Count:',count)