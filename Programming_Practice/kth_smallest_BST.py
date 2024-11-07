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
root.left = Node(1, None, Node(2))
root.right = Node(4)

def kth_smallest(root, k):
    array = []
    def inorder(root):
        if not root:
            return
    
        inorder(root.left)
        array.append(root.val)
        # print(array)
        inorder(root.right)
    inorder(root)
    return array[k-1]
        
kth_smallest(root, 3)



