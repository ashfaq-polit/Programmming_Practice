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
        
root = Node(6)
root.left = Node(2, Node(0), Node(4, Node(3), Node(5)))
root.right = Node(8, Node(7), Node(9))


def LCA(root, p, q):
    # print(root.val)
    while root:
        if p > root.val and q > root.val:
            root = root.right
        elif p < root.val and q < root.val:
            root = root.left
        else:
            return root.val    
        
LCA(root, p = 7, q = 9)


def LCA(root, p, q):
        if p < root.data and q < root.data:
            return LCA(root.left, p, q)
        elif p > root.data and q > root.data:
            return LCA(root.right, p, q)
        else:
            return root.data

        
        
def LCA_binary_tree(root,p,q):
    if root is None:
        return None
    if root.data == p or root.data == q:
        return root
    left_lca = LCA_binary_tree(root.left, p, q)
    right_lca = LCA_binary_tree(root.right, p, q)
    
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca
        
        
        



root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

p = 10
q = 14

t1 = LCA(root, p, q)
print(t1.data)

t2 = LCA_binary_tree(root, p, q)
print(t2.data)