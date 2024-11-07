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
        
root = Node(4)
root.left = Node(2, Node(1), Node(3))
root.right = Node(7, Node(6), Node(9))

# root = Node(2)
# root.left = Node(1)
# root.right = Node(3)

def invert_BT(root):
    if not root:
        return False
    
    if root.left:
        invert_BT(root.left)
        
    if root.right:
        invert_BT(root.right)
        
    if root.left and root.right:
        temp = root.right
        root.right = root.left
        root.left = temp
        
invert_BT(root)

########Print the tree
from collections import deque
q = deque()
q.append(root)
big_list = []

while q:
        popped = q.popleft()
        big_list.append(popped.val)
        if popped.left:
            q.append(popped.left)
        if popped.right:
            q.append(popped.right)
    
    