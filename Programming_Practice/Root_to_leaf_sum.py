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
        
root = Node(5)
root.left = Node(11, Node(4), Node(2))
root.right = Node(3, None, Node(1))

def root_to_leaf_sum(root):
    if not root:
        return 0
    return root.val + max(root_to_leaf_sum(root.left), root_to_leaf_sum(root.right))

root_to_leaf_sum(root)