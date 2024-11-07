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
        
def inorder_traversal(root):
    if root == None:
        return
    else:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root == None:
        return
    else:
        print(root.data)
        preorder_traversal(root.left)
        preorder_traversal(root.right)    
        
def postorder_traversal(root):
    if root == None:
        return
    else:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data)
    
root = Node('A')
root.left = Node('B')
root.left.left = Node('D')
root.left.right = Node('E')
root.right = Node('C')

postorder_traversal(root)