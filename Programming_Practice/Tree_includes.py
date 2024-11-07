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


def Tree_includes_DFS(root, target):
    if root is None:
        return False
    
    #print(root.val)
    if root.val == target:
        return True
    return Tree_includes_DFS(root.left, target) or Tree_includes_DFS(root.right, target)
        
Tree_includes_DFS(root, 7)

    
def Tree_includes_BFS(root, target):
    from collections import deque
    q = deque()
    q.append(root)
    while q:
        popped = q.popleft()
        if popped.val == target:
            return True
        if popped.left:
            q.append(popped.left)
        if popped.right:
            q.append(popped.right)
    return False
    
Tree_includes_BFS(root, 11)