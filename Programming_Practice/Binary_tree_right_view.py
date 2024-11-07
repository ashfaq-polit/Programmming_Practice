#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
from collections import deque

def tree_right_view(root):
    q = deque()
    #stack = []
    cur = root
    q.append(cur)
    res = []

    while q:
        qlen = len(q)
        level = []
        for i in range(qlen):
            cur = q.popleft()           
            level.append(cur.data)
            #print(cur.data)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)  
        #stack.append(level)
        res.append(level[-1])
    return res        
       

root = Node(1)
root.left = Node(2)
root.left.left = Node(5)
root.left.right = Node(4)
root.left.left.left = Node(10)
root.right = Node(7)

tree_right_view(root)