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
root.left = None
root.right = Node(2, Node(3), None)

# root = None

def inorder_traversal(root):
    if not root:
        return []
    
    if root.left:
        inorder_traversal(root.left)
    print(root.val)
    if root.right:
        inorder_traversal(root.right)  
        
inorder_traversal(root)

    