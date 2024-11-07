#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

class Node:
    def __init__(self, data = 0, left = None, right  =None):
        self.data = data
        self.left = left
        self.right = right
        
root = Node(1)
root.left = Node(2, None, Node(5))
root.right = Node(3, None, Node(4))


def right_view(root):
    right_list = []
    
    def dfs(root, right_list, level):
        if not root:
            return 
        if len(right_list) == level:
            right_list.append(root.data)
        
        dfs(root.right, right_list, level+1)
        dfs(root.left, right_list, level+1)
        
    dfs(root, right_list, 0)
    return right_list
 
right_view(root)   
        