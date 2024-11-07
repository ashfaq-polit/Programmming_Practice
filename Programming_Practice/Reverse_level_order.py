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
root.left = Node(9, None, None)
root.right = Node(20, Node(15), Node(7))
# root.left = None
# root.right = Node(3, None, Node(4, None, Node(5, None, Node(6))))

from collections import deque

q = deque()

q.append(root)
bool = True
stack = []
reverse_list = []

while q:
    small_list = []
    for _ in range(len(q)):
        popped = q.popleft()
        small_list.append(popped.val)

        if popped.left:
            q.append(popped.left)
        if popped.right:
            q.append(popped.right) 
                   
    stack.append(small_list)
 
for _ in range(len(stack)):
    reverse_list.append(stack.pop())          
