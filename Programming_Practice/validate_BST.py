#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = Node(2)
root.left = Node(1)
root.right = Node(3)
        
def valid_BST(root):  
    def validate(root, left, right):
        if not root.left and not root.right:
            return True
        if root.val < left or root.val > right:
            return False
        return validate(root.left, left, root.val) and validate(root.right, root.val, right)
    return validate(root, float('-inf'), float('inf') )
        
valid_BST(root)       
        
        
        
        
        
        
        
def validate_BST(root):
    stack = []
    cur = root
    result = []
    left_val = -9999

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur)
        # print(cur.data)
        if cur.data < left_val:
            return False
        left_val = cur.data
        print(left_val)
        cur = cur.right
    return True

def kth_smallest_value(root, k):
    cur = root
    stack = []
    #result = []
    count = 0
    
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        #result.append(cur.data)
        count += 1
        print(cur.data, count)
        if count == k:
            return cur.data
        cur = cur.right 
 


root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.left.left = Node(1)

validate_BST(root)

kth_smallest_value(root, 3)