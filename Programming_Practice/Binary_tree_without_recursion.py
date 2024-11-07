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
        
# class BinaryTree:
#     def __init__(self, root):
#         self.root = Node(root)
        
#     def in_order_traversal(self, root):
#         if root:
#             self.in_order_traversal(root.left)
#             result.append(root.data)
#             self.in_order_traversal(root.right)
#         return 
    
 
def in_order_traversal(root):
    stack = []
    result = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        print("cur1:", cur.data)
        result.append(cur.data)
        cur = cur.right
        #print("cur2:", cur.data)

    print(result)  
    
def pre_order_traversal(root):
          
    stack = []
    result = []
    cur = root
    stack.append(cur)
            
    while len(stack) > 0:
        cur = stack.pop()
        result.append(cur.data)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    print(result)  
    
def post_order_traversal(root):
    
    result = []
    stack1 = []
    stack2 = []
    cur = root
    stack1.append(cur)
    
    while stack1:
        cur = stack1.pop()
        stack2.append(cur)
        if cur.left:
            stack1.append(cur.left)
        if cur.right:
            stack1.append(cur.right)
            
    while stack2:
        popped = stack2.pop()
        print(popped.data)
            
                  

root = Node('A')
root.left = Node('B')
root.left.left = Node('D')
root.left.right = Node('E')
root.right = Node('C')

root = Node(1)
root.left = Node(2)
root.left.left = Node(5)
root.left.right = Node(4)
root.right = Node(7)

in_order_traversal(root)
