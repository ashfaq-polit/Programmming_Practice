#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
root = Node(3)
root.left = Node(11, Node(4), Node(2))
root.right = Node(4, None, Node(1))

def Tree_sum(root):
    if root is None:
        return 0
    return root.val + Tree_sum(root.left) + Tree_sum(root.right)

Tree_sum(root)