#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

n = 6


def Fibonacci(n):
    Fib = [0 for _ in range(n+1)]
    
    Fib[0] = 0
    Fib[1] = 1
    
    total, sum_square = 1, 1
    
    for i in range(2, n + 1):
        Fib[i] = Fib[i-1] + Fib[i-2]
        total += Fib[i]
        sum_square +=  
        
    return Fib[n], Fib[n] % 10, total % 10

Fibonacci(n)