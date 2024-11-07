#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

###Climbing stairs
n = 8

def climbing_stairs(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
        
climbing_stairs(n)


###Coin change
coins = [1,2,5]
amount = 11

def coin_change(coins, amount):
    dp = [(amount+1) for _ in range(amount+1)]
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], 1 + dp[i-c])
    return dp[amount] if dp[amount] != amount+1 else -1

coin_change(coins, amount)


###Maximum subarray
nums = [-2,1,-3,4,-1,2,1,-5,4]

maxm, total = 0, 0
for i in nums:
    total += i
    if total < 0:
        total = 0
    maxm = max(maxm, total)
    
    
###Longest increasing subsequence
nums = [10,9,2,5,3,7,101,18]

def LIS(nums):
    LIS = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
            print(LIS)
    return LIS[len(nums) - 1]

LIS(nums) 


###House Robber
nums = [7,5,3,10]

def house_robber(nums):
    total = nums.copy()
    total[0] = nums[0]
    total[1] = max(total[0], nums[1])
    for i in range(2, len(nums)):
        total[i] = max(total[i] + total[i-2], total[i-1])
        print(total[i])
    return max(total)

house_robber(nums)


###Unique paths
m = 3
n = 2

def unique_paths(m, n):
    grid = [[1] * n] * m
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[m-1][n-1]
 
unique_paths(m, n) 


###Maximum product subarray 
nums = [2,3,-2,-4]

def maxm_prod_subarray(nums): 
    n = len(nums)
    left_prod, right_prod = 1, 1
    maxm = 0
    
    for i in range(n):
        left_prod *= nums[i] 
        right_prod *= nums[n-i-1]
        maxm = max(left_prod, right_prod, maxm)
            
    return maxm
            
        
maxm_prod_subarray(nums)   


###Decode ways
s = "122016"

def decode_ways(s):
    dp = [0] * (len(s) + 1)
    
    dp[0] = 1
    if s[0] == '0':
        dp[1] = 0
    else:
        dp[1] = 1


    for i in range(1, len(s)):
        if s[i] == '0' and s[i-1] in '12':
            dp[i+1] = dp[i-1]
        elif s[i] != '0' and (s[i-1] in '1' or (s[i-1] == '2' and s[i] in '0123456')):
            dp[i+1] = dp[i] + dp[i-1]
        elif s[i] != 0 and s[i-1] == 0:
            dp[i+1]= dp[i]
        else:
             dp[i+1]= dp[i]
        print(dp)
    return dp[len(dp)-1]
        
decode_ways(s)    


###Longest common subsequence   
text1 = "abc"
text2 = "def" 

def LIS(text1, text2):
    dp = [[0 for _ in range(len(text1))] for _ in range(len(text2)+1)]

    for i in range(len(text2)):
        for j in range(len(text1)):
            if text2[i] == text1[j]:
                dp[i+1][j] = 1 + dp[i][j-1]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-1])
    return dp[len(text2)][len(text1)-1]
 
LIS(text1, text2)    


###Word Break
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

def word_break(s, wordDict):
    l, r = 0, 0
    for r in range(len(s)+1):
        for word in wordDict:
            if s[l:r] in wordDict:
                l = r
                print(l, r)
    return True if l == r else False

word_break(s, wordDict)


###House Robber II
nums = [1,2,3,1]

def house_robber(nums):
    dp = nums.copy()
    print(dp)
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i] + dp[i-2], dp[i-1])
    return dp[len(nums) - 1]
    
   
def house_robber_circular(nums):
    dp_start = house_robber(nums[:len(nums) - 1])
    dp_end = house_robber(nums[1:len(nums)])
    return max(dp_start, dp_end)
    
house_robber_circular(nums)        