#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

###########Number of 1 bits
n = 2147483645
count = 0

while n > 0:
    m = n % 2
    n = n // 2
    if m == 1:
        count += 1
        
print(count)
   

###########Counting bits
def counting_bits(n):
    dp = [0 for _ in range(n+1)]
    mult = 1
    
    for i in range(1, n+1):
        if i % 2 == 0:
            mult *= 2
        dp[i] = 1 + dp[i - mult]
        print(dp, mult)
        
    return dp
        
n = 5
counting_bits(n)
        
        
###Add two integeres
def add_two_integers(a, b):
    while b:
        c = a ^ b
        d = (a & b) << 1
        a = c
        b = d
    return a
           
a = 1
b = 2

add_two_integers(a, b)    


###Missing Number
def missing_number(nums):
    maxm = len(nums)
    res1, res2 = 0, 0
    for i in range(maxm+1):
        res1 = res1 ^ i
    for j in range(len(nums)):
        res2 = res2 ^ nums[j]
        
    return res1 ^ res2

nums = [9,6,4,2,3,5,7,0,1]

missing_number(nums)


###Reverse Bits
def reverse_bits(n):
    res = 0
    for i in range(32):
        bit = (n >> i) & 1 
        res = res | (bit << (31 - i))
    return res
    
    
n = 43261596

reverse_bits(n)


def single_number(nums):
    res = 0
    for i in nums:
        res = res ^ i
    return res
    
    
nums = [7,6,6,7,8]
    
single_number(nums)


