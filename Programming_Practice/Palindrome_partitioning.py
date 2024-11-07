#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

def palindrome_partitioning(s):
   res  = []   
   cur = []   
   def backtrack(i):
       if i >= len(s):
           res.append(cur.copy())
           return
       for j in range(i, len(s)):
           if is_palindrome(s, i, j):
               cur.append(s[i:j+1])
               backtrack(i+1)
               cur.pop()
               #backtrack(i+1)

   backtrack(0)
   return res

def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True

s = "aaba"
palindrome_partitioning(s)