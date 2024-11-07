#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

coins = [1,2,5]
amount = 11

def coin_change(coins, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    
    for i in range(1, amount+1):
        for j in range(len(coins)):
            if i >= coins[j]:
                dp[i] = min(dp[i], 1 + dp[i - coins[j]])
            
    return dp[amount] if dp[amount] != amount+1 else -1, dp

coin_change(coins, amount)