#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def set_matrix_zeros(matrix):
    
    rows = len(matrix)
    columns = len(matrix[0])
    
    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] == 0:
                pass
            else:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 
                    

    for j in range(0, columns):
        if matrix[0][j] == 0:
            for j in range(0, columns):
                matrix[0][j] = 0
            
    for i in range(0, rows):
        if matrix[i][0] == 0:
            for i in range(0, rows):
                matrix[i][0] = 0
            
    
    return matrix

set_matrix_zeros(matrix)