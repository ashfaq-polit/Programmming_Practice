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
        
        
def Search_inorder_traversal(root, element):
    if root == None:
        return
    else:
        while root:
            if element < root.data:
                # print(root.data)
                root = root.left                
            elif element > root.data:
                # print(root.data)
                root = root.right 
            else: 
                print('Found')
                return
        print('Not found')

        

        
def insertion_binary_tree(root, data):
     if root == None:
         return Node(data)
     else:
         cur = root
         parent = None
         while cur:
             parent = cur
             if data < cur.data:
                 cur = cur.left
             else:
                 cur = cur.right
                 
         if data < parent.data:
             parent.left = Node(data)
         if data > parent.data:
             parent.right = Node(data)
                 
def insertion_binary_treeR(root, data):
     if root == None:
         root = Node(data)
     else:
         if data < root.data:
             # if root.left:
                 # root = root.left
                  root.left = insertion_binary_treeR(root.left, data)
             # root.left = Node(data)
             
         else:
             # if root.right:
                 # root = root.right
                 root.right = insertion_binary_treeR(root.right, data)
             # root.right = Node(data)
     return root

def insert(root, key):
    if root is None:
        root = Node(key)
    else:
        if root.data < key:
            root.right= insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


             
def inorder_traversal(root):
     if root == None:
         return
     else:
         inorder_traversal(root.left)
         print(root.data)
         inorder_traversal(root.right)        


root = Node(50)
root.left = Node(30)
root.left.left = Node(20)
root.left.right = Node(40)
root.right = Node(70)

Search_inorder_traversal(root, 71)


root = Node(50)
root = insertion_binary_treeR(root, 30)
root = insertion_binary_treeR(root, 20)
root = insertion_binary_treeR(root, 40)
root = insertion_binary_treeR(root, 70)

inorder_traversal(root)

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)

inorder_traversal(r)