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
        
root = Node(2)
root.left = Node(9, None, None)
root.right = Node(20, Node(15), Node(7))
# root.left = None
# root.right = Node(3, None, Node(4, None, Node(5, None, Node(6))))

from collections import deque

q = deque()

q.append(root)
depth = 0
bool = True

while q and bool == True:
    for _ in range(len(q)):
        popped = q.popleft()
        
        if not popped.left and not popped.right:
            bool = False
        if popped.left:
            q.append(popped.left)
        if popped.right:
            q.append(popped.right)                
    depth += 1
            