#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

s = "pwwkew"

Hash_map = []
count = 0
slow = 0
fast = 0

for i in s:
    if i not in Hash_map:
        Hash_map.append(i)
        fast += 1
        count = max(count, fast - slow)
    else:
        slow += 1
        Hash_map = Hash_map[1:]
        
        
######String to integer

s = "4193 with words"
num  = 0
sign = 1

for i in s:
    integer = ord(i) - ord('0')
    if i == '-':
        sign = -1
    if integer > 0 and integer <10:
        num = 10* num + integer
        
num = num * sign
    

#########Longest palindromic substring

s = "babad"

if len(s) % 2 == 0:    
    left = (len(s)//2) -1
    right = len(s)//2
else:
    left = right = len(s)//2
    
max_substr = ''
    
while left>= 0:
    substr = s[left:right+1]
    left -= 1
    right += 1
    print(substr)
    for i in range(len(substr)):
        if substr[i] == substr[len(substr)-i-1]:
            bool = 1           
            if len(substr) > len(max_substr):
                max_substr = substr
        else:
            bool= 0 
            break

            