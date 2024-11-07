#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

prices = [7,1,5,3,6,4]
buy = 0
profit = 0

for sell in range(1, len(prices)):
    if prices[sell] < prices[buy]:
        buy = sell
    else:
        diff = prices[sell] - prices[buy]
        profit = max(profit, diff)
        
print('Profit:', profit)