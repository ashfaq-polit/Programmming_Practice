#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

top = 0
bottom = len(matrix)
left = 0
right = len(matrix[0])

output = []

i = 0
j = 0
while left <right and top < bottom:
    for j in range(left,right):
        output.append(matrix[top][j])
    top += 1
    
    for i in range(top,bottom):
        output.append(matrix[i][right-1])
    right -= 1
    
    if not (left <right and top < bottom):
        break
    
    for j in reversed(range(left,right)):
        output.append(matrix[bottom-1][j])
    bottom -= 1    
    
    for i in reversed(range(top,bottom)):
            output.append(matrix[i][left])
    left += 1
    

####Another way
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

len(matrix) #row
len(matrix[0]) #column


def spiral_matrix(matrix):
    L = 0
    R = len(matrix[0]) 
    T = 0
    B = len(matrix) 
    
    res = []
    
    while L <= R and T <= B:
        for i in range(L, R):
            res.append(matrix[T][i])
        T += 1
        for j in range(T, B - 1):
            res.append(matrix[j][R-1])
        R -= 1
        for k in range(R, L, -1):
            res.append(matrix[B-1][k])
        B -= 1
        for l in range(B, T - 1, -1):
            res.append(matrix[l][L])
        L += 1
    return res
        
        
spiral_matrix(matrix)      
    

        
        
        