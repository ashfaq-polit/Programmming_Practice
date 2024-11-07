#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""
######Find all anagrams
s = "abab"
p = "ab"

p_hash = {}
s_hash = {}

for i in p:
    if i not in p_hash:
        p_hash[i] = 1
    else:
        p_hash[i] += 1
        
for i in s[0:len(p)]:
    if i not in s_hash:
        s_hash[i] = 1
    else:
        s_hash[i] += 1


left = 0
right = len(p)-1
result = [0] if p_hash == s_hash else []

for i in range(len(p), len(s)):
    if s[i] not in s_hash:
        s_hash[s[i]] = 1
    else:
        s_hash[s[i]] += 1

    s_hash[s[left]] -= 1
    if s_hash[s[left]] == 0:
        s_hash.pop(s[left])
    
    if s_hash == p_hash:
        result.append(left+1)
        
    left += 1
    
    
#########Ransom Note
ransomNote = "a"
magazine = "b"  

def ransomnote(ransomNote, magazine):
    mag_hash = {}
    for char in magazine:
        if char not in mag_hash:
            mag_hash[char] = 1
        else:
            mag_hash[char] += 1
            
    for i in ransomNote:
        if i not in mag_hash:
            return False
        else:
            if mag_hash[i] == 0:
                return False
            mag_hash[i] -= 1
    return True
    
ransomnote(ransomNote, magazine)   

        
    