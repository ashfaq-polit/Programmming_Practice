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
        
root = Node(1)
root.left = Node(2, Node(4), Node(5))
root.right = Node(3, Node(6), Node(7))
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

from collections import deque

q = deque()

q.append(root)
big_list = []

while q:
    # small_list = []
    for _ in range(len(q)):
        popped = q.popleft()
        big_list.append(popped.val)
        
        if popped.left:
            q.append(popped.left)
            
        if popped.right:
            q.append(popped.right)
    big_list.append('#')

