#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

###Permutations
def permutations(nums):
    res = []
    subset = []
    backtrack(nums, res, subset)
    return res
            
 
def backtrack(nums,res, subset):
    if len(subset) == len(nums):
        res.append(subset.copy())
        print('res:', res)
        
    for i in range(len(nums)):
        if nums[i] in subset:
            continue
        else:
            subset.append(nums[i])
            print(subset)
            backtrack(nums, res, subset)
            subset.pop()
            print('subseT:', subset)
    
    
nums = [1,2,3]
permutations(nums)



###Subsets
def subsets(nums):
    res = []
    subset = []
    backtrack(nums, res, subset, 0)
    return res

def backtrack(num, res, subset, i):
    res.append(subset.copy())
        
    for i in range(i, len(nums)):
        subset.append(nums[i])
        print(subset)
        backtrack(nums, res, subset, i+1)
        subset.pop()
    
nums = [1,2,3]
subsets(nums)


###Combination Sum
def combination_sum(candidates, target):
    res = []
    subset = []
    backtrack(res, subset, candidates, target, 0)
    return res

def backtrack(res, subset, candidates, target, i):
    if target == 0:
        res.append(subset.copy())
        
    for i in range(i, len(candidates)):
        subset.append(candidates[i])
        print(subset)
        newtarget = target - candidates[i]
        if newtarget >= 0:
            backtrack(res, subset, candidates, newtarget, i)
        subset.pop()
        
    
candidates = [2,3,6,7]
target = 7

combination_sum(candidates, target)


##Combination Sum II
def Combination_Sum2(candidadtes, target):
    res = []
    subset = []
    backtrack(res, subset, candidates, target, 0)
    return res

def backtrack(res, subset, candidates, target, i):
    candidates.sort()
    if target == 0 and subset not in res:
        res.append(subset.copy())
        
    for i in range(i, len(candidates)):
        # if candidates[i] ==  in subset:
        #     continue
        subset.append(candidates[i])
        newTarget = target - candidates[i]
        if newTarget >= 0:
            backtrack(res, subset, candidates, newTarget, i+1)
        subset.pop()
    
 
candidates = [10,1,2,7,6,1,5]
target = 8

Combination_Sum2(candidates, target) 


##Palindrome Partitioning
def Palindrome_Partitioning(s):
    res = []
    subset = []
    backtrack(res, subset, s, 0)
    return res

def backtrack(res, subset, s, i):
    if i >= len(s):
        res.append(subset.copy())
        
    
    for j in range(i, len(s)):
        if is_Palindrome(s, i, j):
            subset.append(s[i:j+1])
            backtrack(res, subset, s, i+1)
            subset.pop()
            
def is_Palindrome(s, l, r):
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
            
   
s = "aca"
Palindrome_Partitioning(s)


###Generate Parentheses
def Generate_Parentheses(n):
    res = []
    subset = ''
    opened, closed = 0, 0 
    backtrack(res, subset, n, opened, closed)
    return res

def backtrack(res, subset, n, opened, closed):
    if opened == n and closed == n:
        res.append(subset)
        # return
    
    if opened < n:
        subset += '('
        # opened += 1
        backtrack(res, subset, n, opened+1, closed) 
        subset = subset[:-1]

    if closed < opened:
        subset += ')'
        # closed += 1
        backtrack(res, subset, n, opened, closed+1) 
        subset = subset[:-1]

    
n = 3
Generate_Parentheses(n)   



###Letter cobinations of Phone Number
def letter_comb_phone_no(digits):
    keyboard = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
                }
    res = []
    subset = ''
    if digits:
        backtrack(res, subset, digits, keyboard, 0)
    return res

def backtrack(res, subset, digits, keyboard, i):
    if len(subset) == len(digits):
        res.append(subset)
        return
        
    for c in keyboard[digits[i]]:
        subset += c
        backtrack(res, subset, digits, keyboard, i+1)
        subset = subset[:-1]
        
       
digits = "23"
letter_comb_phone_no(digits)  







