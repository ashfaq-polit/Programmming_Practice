#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 10:35:22 2022

@author: Ashfaq
"""

array = [7, 3, 4, 2, 6, 1, 5, 10, 8, 12, 16, 15, 20, 19, 11]


for ind in range(len(array)-1):
        min_index = ind
 
        for j in range(ind + 1, len(array)):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        
        # Swapping the elements to sort the array
        
        # temp = array[min_index]
        # array[min_index] = array[ind]
        # array[ind] = temp
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
         
print(array)

    
    

