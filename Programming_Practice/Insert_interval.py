#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
result = []

for i in range(len(intervals)):

    if newInterval[1] < intervals[i][0]:
        result.append(newInterval)
        result = result + intervals[i:]

    elif newInterval[0] > intervals[i][1]:
        result.append(intervals[i])     
        
    else:
        newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    
    print(newInterval)
    print(result)
    
def insert_intervals(intervals, newInterval):
    
    intervals = sorted(intervals, key = lambda x:x[0], reverse = False)
    
    # res = [intervals[0]]
    res = []
    
    for i in range(len(intervals)):
        if intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
        elif intervals[i][0] > newInterval[1]:
            res.append(newInterval)
            return res + intervals[i:]
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
        # res.append(newInterval)
    return res
    
insert_intervals(intervals, newInterval) 
    
    
######Merge intervals
intervals = [[1,3],[2,16],[8,10],[15,18]]
result = []
cur_interval = intervals[0]
result.append(cur_interval)

for i in range(1,len(intervals)):
    if intervals[i][0] <= cur_interval[1]:
        new_interval = [min(intervals[i][0], cur_interval[0]), max(intervals[i][1], cur_interval[1])]
        
        if new_interval[0] == cur_interval[0]:
            result.remove(cur_interval)
            result.append(new_interval)
        cur_interval = new_interval
    else:
        result.append(intervals[i])
        cur_interval = intervals[i] 
        
        
intervals = [[1,4],[4,5]]

def merge_intervals(intervals):
    # intervals = intervals.append(intervals[-1].copy())
    intervals = sorted(intervals, key = lambda x:x[0], reverse = False)
    res = [intervals[0]]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] <= res[-1][1]:
            # res[-1][0] = intervals[i][0]
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])
        print(i, intervals)   
    return res

merge_intervals(intervals) 
        
        
        
#########Sort colors
nums = [2,0,2,1,1,0]
left = 0
mid = 0
right = len(nums)-1

while mid <= right:
    if nums[mid] == 0:
        nums[mid], nums[left] = nums[left], nums[mid]
        mid += 1
        left += 1
    elif nums[mid] == 2:
        nums[mid], nums[right] = nums[right], nums[mid]
        right -= 1
    else:
        #nums[mid] == 1:
        mid += 1
        
       
        
        
        
        
        
        
        
        
        
        
        