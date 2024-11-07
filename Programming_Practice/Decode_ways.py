#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

import numpy as np
s = "2220"

def decode_ways(s):
    dp = np.ones(len(s)+1)
    for i in range(len(s)-1, -1, -1):
        print(i)
        if s[i] == '0':
            dp[i] = 0           
        if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
            dp[i] = dp[i+1] + dp[i+2]
    return dp[0], dp

