#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

class Node:
    def __init__(self, data = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


root = Node(1)
root.left = Node(2, None, Node(5))
root.right = Node(3, None, Node(4))



from collections import deque
left_list = []

def left_view_BFS(root):
    q = deque()
    q.append(root)
    while q:
        if not root:
            return 
        qlen = len(q)
        level = []
        for i in range(qlen):
            popped = q.popleft()
            level.append(popped.data)
            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)
        left_list.append(level[0])
    return left_list
                
left_view_BFS(root)   


def left_view_DFS(root):
    left_list = []

    def left_view(root, left_list, level):
        if not root:
            return
        if len(left_list) == level:
            left_list.append(root.data)
            
        left_view(root.left, left_list, level+1)
        left_view(root.right, left_list, level+1)
    
    left_view(root, left_list, 0)
    return left_list
        
left_view_DFS(root)    



list = [0 for _ in range(3)]