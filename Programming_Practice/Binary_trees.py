#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

        
def max_depth(root):
    if not root:
        return 0
    else:
        return 1 + max(max_depth(root.left), max_depth(root.right))
        
root = Node(3)
root.left = Node(9)
root.right = Node(20, Node(15), Node(7))
    
max_depth(root)


###Same tree
p = [1,2,3]
q = [1,2,3]

root1 = Node(1, Node(2), Node(3))
root2 = Node(1, Node(3), Node(2))

def same_tree(root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.data != root2.data:
            return False
        return same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)

same_tree(root1, root2)


###Invert_binary_tree
def invert_binary_tree(root):
    
    if not root:
        return None

        temp = root.left
        root.left = root.right
        root.right = temp
        
        invert_binary_tree(root.left)
        invert_binary_tree(root.right)
        
    return root
    
        
# root = [4,2,7,1,3,6,9]
root = Node(4)
root.left = Node(2, Node(1), Node(3))
root.right = Node(7, Node(6), Node(9))

invert_binary_tree(root)



###Maximum path sum
def maximum_path_sum(root):
    res = 0
    if not root:
        return 0
    maxm = max(root.data, root.data+root.left.data, root.data+root.right.data)
    res = max(res, maxm)
    res = max(maximum_path_sum(root.left), maximum_path_sum(root.right))
    return res
        
root = Node(-10)  
root.left = Node(9)  
root.right = Node(20, Node(15), Node(7))

maximum_path_sum(root)


###Level_order_traversal
def level_order_traversal(root):
    from collections import deque
    queue = deque()
    biglist = []
    queue.append(root)
    while queue:
        qlen = len(queue)
        smalllist = []
        for i in range(qlen):
            temp = queue.popleft()
            smalllist.append(temp.data)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        biglist.append(smalllist)
        
    return biglist
        
        
       
root = Node(3)  
root.left = Node(9)  
root.right = Node(20, Node(15), Node(7))

level_order_traversal(root)


###Subtree of another tree
def subtree(root, subroot):
    if not subroot:
        return True
    if not root:
        return False
    if same_tree(root, subroot):
        return True
    return subtree(root.left, subroot) or subtree(root.right, subroot)
    
    
root = Node(3)
root.left = Node(4, Node(1), Node(2))
root.right = Node(5)

subroot = Node(4, Node(1), Node(2))

subtree(root, subroot)


###Construct Binary Tree from Preorder and Inorder Traversal
def tree_from_preorder_inorder(preorder, inorder):
    if not preorder or not inorder:
        return None
    root = Node(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = Node(tree_from_preorder_inorder(preorder[1:mid+1], inorder[:mid]))
    root.right = Node(tree_from_preorder_inorder(preorder[mid+1:], inorder[mid+1:]))
    return level_order_traversal(root)
    
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

tree_from_preorder_inorder(preorder, inorder)


###Validate Binary Search Tree
def validate_BST(root):
    if not root:
        return True
    llist = []
    llist = inorder_traversal(root, llist)
    if llist == sorted(llist):
        return True
    else:
        return False
    
def inorder_traversal(root, llist):
    if not root:
        return None
    inorder_traversal(root.left, llist)
    llist.append(root.data)
    inorder_traversal(root.right, llist)
    return llist
    
#root = [2,1,3]
root = Node(5)
root.left = Node(1)
root.right = Node(8, Node(6), Node(9))

validate_BST(root)


###K-th smallest element in BST
def kth_smallest_BST(root, k):
    llist = []
    llist = inorder_traversal(root, llist)
    llist = sorted(llist)
    return llist[k-1]


root = Node(5)
root.left = Node(3, Node(2, Node(1), None), Node(4))
root.right = Node(6)

kth_smallest_BST(root, 3)



###Lowest common ancestor
def LCA_bst(root, p, q):
    while root:
        if p < root.data and q < root.data:
            root = root.left
        elif p > root.data and q > root.data:
            root = root.right
        else:
            return root.data
            
    
root = Node(6)
root.left = Node(2, Node(0), Node(4, Node(3), Node(5)))
root.right = Node(8, Node(7), Node(9))

LCA_bst(root, 2, 4)



###Implememnt Prefix Tree
class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    
class Trie:
    def __init__(self):
        self.root = Node()
        

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            else:
                cur = cur.children[c]
        cur.endOfWord = True
        

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return cur.endOfWord
        

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.chidlren:
                return False
            else:
                cur = cur.children[c]
        return True
            
        
        
        
trie = Trie()
trie.insert("apple")
trie.search("apple") 
trie.search("app")    
trie.startsWith("app") 
trie.insert("app");
trie.search("app"); 