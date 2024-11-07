#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 13:53:57 2022

@author: Ashfaq
"""

array = [7, 3, 4, 2, 6, 1, 5, 10, 8, 12, 16, 15, 20, 19, 11]


def merge_sort(array):
    # if len(array) <=1:
    #     return array
    if len(array) > 1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]
        
        merge_sort(left_array)
        merge_sort(right_array)
        
        i=0 #index for left array
        j=0 #index for right array
        k=0 #index for the combined/original array

        while i<len(left_array) and j<len(right_array):
            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                i+=1
            else:
                array[k] = right_array[j]
                j+=1
            k+=1
            
        while i<len(left_array):
            array[k] = left_array[i]
            i+=1
            k+=1
            
        while j<len(right_array):
            array[k] = right_array[j]
            j+=1
            k+=1
        return array
                
       
array_sorted = merge_sort(array)
print(array_sorted)


#############Merge two sorted arrays###########
array1 = [1, 2, 3, 56, 89]
array2 = [2, 5, 6]

def merge_sorted_array(array1, array2):
    count1=0
    count2=0
    new_array = []
    
    while count1<len(array1) and count2<len(array2):
        if array1[count1]<=array2[count2]:
            new_array.append(array1[count1])
            count1 +=1
        else:
            new_array.append(array2[count2])
            count2 +=1
    
    while count1<len(array1):
            new_array.append(array1[count1])
            count1 +=1
            
    while count2<len(array2):
            new_array.append(array2[count2])
            count2 +=1 
            
    print(new_array)
        
          
merge_sorted_array(array1, array2)

