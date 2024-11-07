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
        
        
def Construct_binary_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root = Node(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = Construct_binary_tree(preorder[1:mid+1],inorder[0:mid])
    root.right = Construct_binary_tree(preorder[mid+1:],inorder[mid+1:])
    return root

def inorder_traversal(root):
     if root == None:
         return
     else:
         inorder_traversal(root.left)
         print(root.data)
         inorder_traversal(root.right) 
         
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

root = Construct_binary_tree(preorder, inorder)
inorder_traversal(root)