#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

s = "babab"

longest = ''
reslen = 0

for i in range(len(s)-1):
    if len(s) % 2 != 0:
        l, r = i, i
        while l >= 0 and r < len(s)  and s[l] == s[r]:
            if (r - l + 1) > reslen:
                longest = s[l:r+1]
                reslen = r - l + 1
                print(reslen)
            l -= 1
            r += 1
    else:
            l, r = i, i + 1
            while l >= 0 and r < len(s)  and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    longest = s[l:r+1]
                    reslen = r - l + 1
                    print(reslen)
                l -= 1
                r += 1

    
        
    