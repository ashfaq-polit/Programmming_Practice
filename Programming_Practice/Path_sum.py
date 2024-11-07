#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
root = Node(5)
root.left = Node(4, Node(11, Node(7), Node(2)), None)
root.right = Node(8, Node(13), Node(4, None, Node(1)))
# root.left = None
# root.right = Node(3, None, Node(4, None, Node(5, None, Node(6))))



def path_sum(root, targetSum):
    if not root:
        return False

    newTarget = targetSum - root.val
    #print(remain)
    
    if not root.left and not root.right and newTarget == 0:
        return True

    return path_sum(root.left, newTarget) or path_sum(root.right, newTarget)
        
    # if not root:
    #     return False
    # if not root.left and not root.right:
    #     return targetSum - root.val == 0
    # return path_sum(root.left, targetSum - root.val) or path_sum(root.right, targetSum - root.val)

targetSum = 22
path_sum(root, 22)