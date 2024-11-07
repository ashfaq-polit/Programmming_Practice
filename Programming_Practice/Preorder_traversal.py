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
        
root = Node(1)
root.left = Node(4, Node(8), Node(6))
root.right = Node(2, Node(3), Node(7))
#root = []

def preorder(root):
    if not root:
        return []
    
    print(root.val)
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)
        
preorder(root)

