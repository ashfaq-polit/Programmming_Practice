#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10

boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse= True)

total = 0
boxNo = 0
for i in range(len(boxTypes)):
    prev_box = boxNo
    boxNo = boxNo + boxTypes[i][0]
    if boxNo <= truckSize:
        total += boxTypes[i][0] * boxTypes[i][1]
    else:
        total += (truckSize - prev_box) * boxTypes[i][1]
        break
    print(total)    
        
print('Total:', total)
    
    