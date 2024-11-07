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
root.left = Node(9)
root.right = Node(20, Node(15), Node(7))

# root = None

def Maximum_depth_BFS(root):
    from collections import deque
    q = deque()
    q.append(root)
    depth = 0
    
    while q:
        for _ in range(len(q)):
            popped = q.popleft()
            if popped.left:
                q.append(popped.left)
            if popped.right:
                 q.append(popped.right)    
        depth += 1
    return depth

Maximum_depth_BFS(root)

def Maximum_depth_DFS(root): 
    if not root:
        return 0
    
    return 1 + max(Maximum_depth_DFS(root.left), Maximum_depth_DFS(root.right))  
        
Maximum_depth_DFS(root)