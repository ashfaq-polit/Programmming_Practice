#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 12:30:41 2022

@author: Ashfaq
"""

array = [7, 3, 4, 2, 6, 1, 5, 10, 8, 12, 16, 15, 20, 19, 11]


for ind in range(len(array)-1):
 
        for j in range(len(array)-1-ind):

            if array[j+1] < array[j]:
                (array[j], array[j+1]) = (array[j+1], array[j])
 
         
print(array)