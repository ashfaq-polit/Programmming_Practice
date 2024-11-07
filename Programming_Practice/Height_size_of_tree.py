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
        
def Size_inorder_traversal(root):
    if root == None:
        return
    else:
        cur = root
        stack = []
        count = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left 
            cur = stack.pop()
            count += 1
            cur = cur.right 
        return count
 
#########Recursive approach
# def Size_inorder_traversal(root):
#     if root == None:
#         return
#     else:
#         return Size_inorder_traversal(root.left) + 1 + Size_inorder_traversal(root.right)
    
def Height_inorder_traversal(root):
    if root == None:
        return 0
    else:
        # cur = root
        # stack = []
        # count_left = 0
        # count_right = 0
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left 
        #         if cur:
        #             count_left += 1
        #     cur = stack.pop()
        #     cur = cur.right 
        #     if cur:
        #         count_right += 1
        # return 1 + max(count_left, count_right)
        return 1 + max(Height_inorder_traversal(root.left), Height_inorder_traversal(root.right))
    
def Diameter_binary_tree(root):
    max = 0
    if root == None:
        return -1
    else:   
        lheight = Height_inorder_traversal(root.left)
        rheight = Height_inorder_traversal(root.right)
 
    # Get the diameter of left and right sub-trees
        ldiameter = Diameter_binary_tree(root.left)
        rdiameter = Diameter_binary_tree(root.right)
 
    # Return max of the following tree:
    # 1) Diameter of left subtree
    # 2) Diameter of right subtree
    # 3) Height of left subtree + height of right subtree +1
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))
        
    
def Balanced_Binary_Tree(root):
    if root == None:
        return 0
    else:
        lh = Balanced_Binary_Tree(root.left)
        rh = Balanced_Binary_Tree(root.right)
        
        if lh or rh or abs(lh-rh) > 1:
            return False
        else:
            return 1 + max(lh, rh)
    return True
    
root = Node('A')
root.left = Node('B')
root.left.left = Node('D')
root.left.right = Node('E')
root.left.right.right = Node('F')
root.right = Node('C')

Size_inorder_traversal(root)
Height_inorder_traversal(root)     


root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(3)
root.left.left.left = Node(4)
root.left.left.right = Node(4)
root.right = Node(2)


Balanced_Binary_Tree(root)  

Diameter_binary_tree(root)         