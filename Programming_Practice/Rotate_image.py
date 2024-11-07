#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""


matrix = [[1,2,3],[4,5,6],[7,8,9]]

def rotate_image(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    L = 0
    R = cols - 1
    
    while L < R:
        for i in range(L, R):
            T, B = L, R
            temp = matrix[T][L+i]
            matrix[T][L+i] = matrix[B-i][L]
            matrix[B-i][L] = matrix[B][R-i]
            matrix[B][R-i] = matrix[T+i][R]
            matrix[T+i][R] = temp            
            
        L += 1
        R -= 1
        # T += 1
        # B -= 1
        
    return matrix
                                                
rotate_image(matrix)  