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
        # self.next = next
        
root = Node(3)
root.left = Node(9, None, None)
root.right = Node(20, Node(15), Node(7))
#root.left = None
#root.right = Node(2)


from collections import deque

q = deque()

q.append(root)
big_list = []

while q:
    small_list = []
    small_list_sum = 0
    for _ in range(len(q)):
        popped = q.popleft()
        small_list.append(popped.val)
        small_list_sum += popped.val
        
        if popped.left:
            q.append(popped.left)           
        if popped.right:
            q.append(popped.right)
            
    avg = small_list_sum / len(small_list)
    big_list.append(avg)
    
print('Average:', big_list)