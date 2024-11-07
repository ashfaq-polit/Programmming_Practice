#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

class Node():
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
root = Node(3)
root.left = Node(9, None, None)
root.right = Node(20, Node(15), Node(7))
#root.left = None
#root.right = Node(2)

########BFS approach
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
    
print('Depth:', depth)


########DFS approach
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

max_depth(root)
