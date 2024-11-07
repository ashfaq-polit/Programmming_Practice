#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""
import numpy as np
m = 3
n = 7


import numpy as np
def unique_paths(m, n):
    dp = np.zeros((m, n))
    dp[0, :] = 1
    dp[:, 0] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i, j] = dp[i - 1, j] + dp[i, j-1]
    return dp[m - 1, n - 1], dp
    
unique_paths(m, n)