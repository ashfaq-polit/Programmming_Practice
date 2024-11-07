#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
    
if sum(gas) < sum(cost):
    print(-1)
else:
    l = 0
    total = 0
    for r in range(len(gas)):
        total += gas[r] - cost[r]
        if total < 0:
            total = 0
            l += 1
    print('index:',l)
    
    

def gas_station(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    else:
        total, l  = 0, 0 
        for r in range(len(gas)):
            supply = gas[r] - cost[r]
            if supply < 0:
                total = 0
                l = r + 1
            else:
                total += supply
        return l 
            

        