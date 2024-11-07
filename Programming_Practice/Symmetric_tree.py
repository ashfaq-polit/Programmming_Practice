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
# root.left = Node(2, Node(3), Node(4))
# root.right = Node(2, Node(4), Node(3))
root.left = Node(2, None, Node(3))
root.right = Node(2, None, Node(3))

def symmetric(root):
    def isymmetric(left, right):
        if not left and not right:
            return True
        if (left and not right) or (not left and right):
            return False
        return (left.val == right.val and
                isymmetric(left.left, right.right) and
                isymmetric(left.right, right.left))       
    return isymmetric(root.left, root.right)
        
symmetric(root)        


######BFS approach
from collections import deque
q = deque()

q.append(root)
bool = True

while q:
    small_list = []
    for _ in range(len(q)):
        popped = q.popleft()
        small_list.append(popped.val)
        print(small_list)
        
        if popped.left:
            q.append(popped.left)
            
        if popped.right:
            q.append(popped.right) 


    l, r = 0, len(small_list) - 1
    while l <= r:
        if small_list[l] != small_list[r]:
            bool = False
            break
        else:
            l += 1
            r -= 1
        
        


            