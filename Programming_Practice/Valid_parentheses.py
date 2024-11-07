#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

s = "(]"


def valid_parenthese(s):
    while True:
        if '()' in s:
            s = s.replace('()', '')
        if '{}' in s:
            s = s.replace('{}', '')
        if '[]' in s:
            s = s.replace('[]', '')   
        else:
            return not s
    
valid_parenthese(s)
