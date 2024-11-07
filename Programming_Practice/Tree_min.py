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
root.left = Node(11, Node(2), Node(15))
root.right = Node(3, None, Node(1))

def Tree_min_BFS(root):
    minm = float('inf')
    from collections import deque
    q = deque()
    q.append(root)
    while q:
        popped = q.popleft()
        if popped.val < minm:
            minm = popped.val 
        if popped.left:
            q.append(popped.left)
        if popped.right:
            q.append(popped.right)
    return minm

Tree_min_BFS(root)

def Tree_min_DFS(root):
    if root is None:
        return float('inf')
    return min(root.val, Tree_min_DFS(root.left), Tree_min_DFS(root.right))

Tree_min_DFS(root)