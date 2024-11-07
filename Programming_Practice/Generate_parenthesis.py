#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

def generate_parenthesis(n):
    res = []
    cur = []
    def backtrack(openC, closeC):
        if openC == closeC ==n:
            res.append("".join(cur))
            return
        if openC < n:
            cur.append("(")
            backtrack(openC + 1, closeC)
            cur.pop()
        if closeC < openC:
            cur.append(")")
            backtrack(openC, closeC + 1)
            cur.pop()
    backtrack(0, 0)
    return res
    
    
n = 3
generate_parenthesis(n)