#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque as queue

     
def level_order_traversal(root):
    q = queue()
    cur = root
    q.append(cur)
    result = []
    while q:
        qlen = len(q)
        print(qlen)
        level = []
        for i in range(qlen):
            cur = q.popleft()
            level.append(cur.data)
        #print(cur.data)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        result.append(level)
    return result

    
def serialize(root):
    if not root:
        return 'N'
    else:
        left = serialize(root.left)
        right = serialize(root.right)
    return str(root.data) + ',' + left + ',' + right 
        

def reverse_level_order_traversal(root):
    q = queue()
    stack = []
    cur = root
    q.append(cur)
    while len(q)!=0:
        cur = q.popleft()
        stack.append(cur)
        if cur.right:
            q.append(cur.right)
        if cur.left:
            q.append(cur.left)
    
    while stack:
        popped = stack.pop()
        print(popped.data)
    

root = Node(50)
root.left = Node(30)
root.left.left = Node(20)
root.left.right = Node(40)
root.right = Node(70)

level_order_traversal(root)
reverse_level_order_traversal(root)

serialize(root)

