#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

s = "A man, a plan, a canal: Panama"

# def valid_palindrome(s):
#     s = s.lower()
             
#     s = ['' if not i.isalpha() else i for i in s]
#     clean_string = "".join(s)
    
#     mid = len(clean_string)//2
    
#     for i in range(mid):
#         if not clean_string[i] == clean_string[-i-1]:
#             return False
#     return True

def valid_palindrome(s):
    s = s.lower()
             
    s = ['' if not i.isalpha() else i for i in s]
    clean_string = "".join(s)
    print(clean_string)
    
    l = 0
    r = len(clean_string) - 1
    
    while l <= r:
        if clean_string[l] != clean_string[r]:
            return False
        else:
            l += 1
            r -= 1
    return True
        
valid_palindrome(s)


#######Valid anagram
s = "anagram"
t = "nagaram"

for i in range(len(t)):
    for j in range(len(s)):
        if t[i] == s[j]:
            s = s[0:j] + s[j+1:len(s)]
            print(s)
            break
 
if s == '':
    print('anagram')
else:
    print('Not anagram')
    
#######Using hash map
s = "anagram"
t = "nagaram"

from collections import Counter
hash_map_s = {}
hash_map_t = {}
for i in s:
    if i not in hash_map_s:
        hash_map_s[i] = 1
    else:
        hash_map_s[i] += 1
        
for i in t:
    if i not in hash_map_t:
        hash_map_t[i] = 1
    else:
        hash_map_t[i] += 1
        
if Counter(hash_map_s) == Counter(hash_map_t):
    print('anagram')
else:
    print('Not anagram')
              
            
        
        
        