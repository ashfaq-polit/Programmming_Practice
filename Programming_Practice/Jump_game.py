#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

nums = [1,3,2,0,2]

reachable = 0
i = 0

# while i < len(nums)-1:
#     reachable += nums[i]
#     print(reachable)
#     i = reachable
#     if reachable == len(nums)-1:
#         print(True)
#         break
#     if nums[reachable]==0:
#         print(False)
#         break

 # Inspired from https://www.youtube.com/watch?v=muDPTDrpS28   
bool = True
for i in range(len(nums)):
    if reachable < i:
        bool = False
    else:
        reachable = max(reachable, i+nums[i])
        print('x:',i+nums[i])
        print(reachable)
        if reachable >= len(nums):
            bool = True
            
        
nums = [3,2,1,0,4]
# [2,3,1,1,4]

def jump_game(nums):
    target = len(nums) - 1
    new_target = target - 1
    
    while target > 0 and new_target >= 0:
        if nums[new_target] >= target - new_target:
            target = new_target
        # else:
        #     target = target
        print(target, new_target)
        new_target -= 1
    return True if target == 0 else False

jump_game(nums)   
