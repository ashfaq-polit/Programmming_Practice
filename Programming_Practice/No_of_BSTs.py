#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

n = 3

def No_of_trees(n):
    
    numTree = [1] * (n+1)

    for i in range(2, n+1):
        total = 0
        for node in range(1, i+1):
            left = node - 1 
            right = i - node
            total += numTree[left] * numTree[right]
        numTree[i] = total
    return numTree[n]

No_of_trees(n)