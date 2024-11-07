#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

def Unique_BST(n):
    n_BST = [1] * (n+1)

    
    for i in range(2, n+1):
        total = 0
        for j in range(1, i+1):
            left = j - 1
            right = i - j
            total += n_BST[left] * n_BST[right]
        n_BST[i] = total 
    return n_BST[n]
    
            

n = 3
Unique_BST(n)