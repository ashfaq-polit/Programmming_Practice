#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""


def twoSum(nums, target):
    hashMap = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashMap:
            return [hashMap[diff], i]
        else:
            hashMap[nums[i]] = i
            
nums = [4,5,6]
target = 10

twoSum(nums, target)


def valid_anagram(s, t):
    hashMapS, hashMapT = {}, {}
    
    for c in s:
        if c not in hashMapS:
            hashMapS[c] = 1
        else:
            hashMapS[c] += 1
            
    ##First way        
    # for c in t:
    #     if c not in hashMapT:
    #         hashMapT[c] = 1
    #     else:
    #         hashMapT[c] += 1
            
    # return hashMapS == hashMapT

    ##Second way
    for j in t:
        if j not in hashMapS:
            return False
        else:
            hashMapS[j] -= 1
    
    return all(value == 0 for value in hashMapS.values())

s = "anagram"
t = "nagaram"
valid_anagram(s, t)


def contains_duplicate(nums):
    hashMap = {}
    for i in nums:
        if i not in hashMap:
            hashMap[i] = 1
        else:
            return True
    return False
        
   
nums = [1,2,3,4]
contains_duplicate(nums)


def buy_sell_stock(prices):
    l, r, maxm = 0, 1, 0
    while r < len(prices):
        profit = prices[r] - prices[l]
        if profit < 0:
            l = r
        else:
            maxm = max(maxm, profit)
        r += 1
    return maxm
               
    
prices = [7,1,5,3,6,4]
buy_sell_stock(prices)


def maximum_subarray(nums):
    l, r, total, largest = 0, 0, float('-inf'), float('-inf')
    while r < len(nums):
        total = sum(nums[l:r+1])
        print(total)
        if total < 0:
            l = r + 1
        largest = max(largest, total)
        r += 1
    return largest
        
        
nums = [2,-3,4,-2,2,1,-1,4]
maximum_subarray(nums)



def max_product_subarray(nums):
    max_prod, cur_prod = float('-inf'), 1
    for i in nums:
        if i == 0:
            cur_prod = 1
            max_prod = max(0, max_prod)
        else:
            cur_prod *= i
            # min_prod = min(min_prod, cur_prod)
            max_prod = max(max_prod, cur_prod)
    return max_prod
        
    
nums = [-2,0,-1,-2]
max_product_subarray(nums)


def product_except_self(nums):
    left_prod, right_prod, final_prod = [1] * len(nums), [1] * len(nums), [1] * len(nums)
    for i in range(1, len(nums)):
        left_prod[i] = left_prod[i-1] * nums[i-1]
    for j in range(len(nums)-2, -1, -1):
        right_prod[j] = right_prod[j+1] * nums[j+1]
    for k in range(len(nums)):
        final_prod[k] = left_prod[k] * right_prod[k]
    return final_prod

def product_except_self(nums):
    final_prod = [1] * len(nums)
    for i in range(1, len(nums)):
        final_prod[i] = final_prod[i-1] * nums[i-1]
    right_prod = 1
    for j in range(len(nums)-2, -1, -1):
        right_prod = right_prod * nums[j+1]
        final_prod[j] = final_prod[j] * right_prod
    return final_prod
        
       
nums = [1,2,3,4]
product_except_self(nums)



def rotated_sorted_array_minm(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        # elif nums[mid] < nums[mid-1]:
        #     return nums[mid] 
        elif nums[mid] >= nums[l]:
            l = mid + 1
        elif nums[mid] < nums[l]:
            r = mid - 1

    #O(n) solution
    # for i in range(len(nums)):
    #     if nums[i] < nums[i-1]:
    #         return nums[i]
        
   
nums = [3,4,5,1,2] #[11,13,15,17]
rotated_sorted_array_minm(nums)



def search_rotated_array(nums):
    l , r = 0, len(nums) -1 
    while l <= r:
        mid = (l+r) // 2
        if target == nums[mid]:
            return mid
        if nums[mid] >= nums[l]:
            if target < nums[l] or target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target > nums[r] or target < nums[mid]:
                r = mid - 1                
            else:
                l = mid + 1
            
    return -1
        
                
nums = [4,5,6,7,0,1,2]
target = 0

search_rotated_array(nums)


def threesum(nums):
   res = []
   nums.sort()
   for i in range(len(nums)):
       if i > 0 and nums[i] == nums[i-1]:
           continue
       else:
           l, r = i+1, len(nums) - 1
           while l < r:
               if nums[i] + nums[l] + nums[r] > 0:
                   r -= 1
               elif nums[i] + nums[l] + nums[r] < 0:
                   l += 1
               else:
                   res.append([nums[i], nums[l], nums[r]])
                   l += 1
                   r -= 1

   return res
                 
            
nums = [-1,0,1,2,-1,-4]
threesum(nums)



def container_most_water(height):
    l, r = 0, len(height) - 1
    maxwater = float('-inf')
    while l < r:
        water = (r-l) * min(height[l], height[r])
        maxwater = max(maxwater, water)
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return maxwater
        
            
height = [1,8,6,2,5,4,8,3,7]
container_most_water(height)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def linked_list_middle(root):
    l, r = root, root
    while r and r.next:
        l = l.next
        r = r.next.next
    return l.data
    
        
# head = [1,2,3,4,5,6]
root = Node(1)
root.next = Node(2)
root.next.next = Node(10)
root.next.next.next = Node(20)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)

linked_list_middle(root)




def linked_list_cycle(root):
    l, r = root, root
    while r and r.next:
        l = l.next
        r = r.next.next
        if l == r:
            return True
    return False
    
# head = [3,2,0,-4], pos = 1    
root = Node(1)
root.next = Node(2)
root.next.next = Node(0)
root.next.next.next = Node(-4)
root.next.next.next.next = root.next

linked_list_cycle(root)
    
   



def remove_nth_node_linked_list(root, n):
    dummy = Node(0)
    dummy.next = root
    
    l, r = dummy, dummy
    count = 0
    while count <= n:
        r = r.next
        count += 1
    
    while r:
        l = l.next
        r = r.next
        
    l.next = l.next.next
    # l.next.next = None
                            
    return traverse_linked_list(dummy.next)
    
def traverse_linked_list(root):
     llist = []
     if not root:
         return []
     else:
         while root:            
             print(root.data)
             llist.append(root.data)
             root = root.next
     return llist
    
root = Node(1)   
root.next = Node(2)
root.next.next = Node(10)
root.next.next.next = Node(4) 
root.next.next.next.next = Node(5) 
n = 2

remove_nth_node_linked_list(root, n)

traverse_linked_list(root)



def reverse_linked_list(root):
    prev, cur = None, root
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        
    return traverse_linked_list(prev)
    
        
root = Node(1)   
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4) 
root.next.next.next.next = Node(5) 

reverse_linked_list(root)



def reorder_linked_list(root):
    if not root or not root.next:
        return root
    
    l, r = root, root
    while r and r.next:
        l = l.next
        r = r.next.next
    # return l.data
    
    prev, cur = None, l.next
    l.next = None
    
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        
    # return traverse_linked_list(prev)

    p1 = root
    p2 = prev
    
    while p2:
        temp1 = p1.next
        temp2 = p2.next
        p1.next = p2
        p1 = temp1
        p2.next = p1
        p2 = temp2
        
    return traverse_linked_list(root)
    
    
root = Node(1)   
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4) 
root.next.next.next.next = Node(5) 

reorder_linked_list(root)



def merge_two_sorted_list(root1, root2):
    head = dummy = Node(0)
    
    while root1 and root2:
        if root1.data < root2.data:
            dummy.next = root1
            root1 = root1.next
        else:
            dummy.next = root2
            root2 = root2.next
        dummy = dummy.next
            
    if root1:
        dummy.next = root1
        
    if root2:
        dummy.next = root2
        
    return traverse_linked_list(head.next)


root1 = Node(1)   
root1.next = Node(2)
root1.next.next = Node(4)

root2 = Node(1)   
root2.next = Node(3)
root2.next.next = Node(4)

merge_two_sorted_list(root1, root2)    


###Doubly linked list
class Node2:
    def __init__(self, data):
        self.data = data
        self.prev= None
        self.next = None
        
def insert_begin_doublellist(root, data):
    newNode = Node2(data)
    newNode.next = root
    root.prev = newNode
    return traverse_linked_list(newNode)

def insert_end_doublellist(root, data):
    cur = root
    while cur and cur.next:
        cur = cur.next
    
    newNode = Node2(data)
    cur.next = newNode
    newNode.prev = cur
    return traverse_linked_list(root)

def delete_begin_doublellist(root):
    root.next.prev = None
    second = root.next 
    root.next = None
    return traverse_linked_list(second)

def delete_end_doublellist(root):
    cur = root
    while cur and cur.next:
        cur = cur.next
    cur.prev.next = None
    cur.prev = None
    return traverse_linked_list(root)
        
root = Node2(1)
l1 = Node2(2)
l2 = Node2(4)

root.next = l1
l1.next = l2

l1.prev = root
l2.prev = l1

insert_begin_doublellist(root, 3)

insert_end_doublellist(root, 3)

delete_begin_doublellist(root)

delete_end_doublellist(root)




def merge_intervals(intervals):
    intervals.sort(key = lambda x:[x[0],x[1]])
    
    res = [intervals[0]]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(intervals[i][1], res[-1][1])
        else:
            res.append(intervals[i])
            
    return res
        
intervals = [[1,3],[8,10],[2,6],[2,4],[15,18]]
merge_intervals(intervals)
        



def non_overlapping_intervals(intervals):
    intervals.sort(key = lambda x:x[0])
    count = 0
    prevEnd = intervals[0][1]
    
    for i in range(1,len(intervals)):
        if intervals[i][0] < prevEnd:
            count += 1
            prevEnd = min(prevEnd, intervals[i][1])
        else:
            prevEnd = intervals[i][1]
    return count
            

intervals = [[1,5],[4,6],[2,3]]
non_overlapping_intervals(intervals)


def insert_interval(intervals, newInterval):
    res = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
        print(res)
    return res
    
    
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]   

insert_interval(intervals, newInterval) 


class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
def binary_tree_depth(root):
    if not root:
        return 0
    else:
        return 1 + max(binary_tree_depth(root.left), binary_tree_depth(root.right))
    
    
root = Node(3)
root.left = Node(9)
root.right = Node(20, Node(15), Node(7))
# root.right.left = Node(15)
# root.right.right =  Node(7)

binary_tree_depth(root)


def binary_tree_diameter(root):
    max_dia = 0
    def dfs(cur):
        nonlocal max_dia
        if not cur:
            return 0
        else:
            dia = dfs(cur.left) + dfs(cur.right)
            max_dia = max(max_dia, dia)  
        return 1 + max(dfs(cur.left), dfs(cur.right))
    
    dfs(root)
    return max_dia
    
root = Node(1)
root.left = Node(2, Node(4, Node(6), Node(7)), Node(5, Node(8), Node(9)))
root.right = None
    
binary_tree_diameter(root)



def invert_binary_tree(root):
    if not root:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    
    invert_binary_tree(root.left)
    invert_binary_tree(root.left)
    
    return root
    
root = Node(4)
root.left = Node(2, Node(1), Node(3))
root.right = Node(7, Node(6), Node(9))

invert_binary_tree(root)



def balanced_tree(root):
    def dfs(cur):
        if not cur:
            return 0
        left = dfs(cur.left)
        right = dfs(cur.right)
        return 1 + max(left, right)
    return abs(dfs(root.left) - dfs(root.right)) <= 1
    
root = Node(3)
root.left = Node(9)
root.right = Node(20, Node(15), Node(7, Node(8)))    

balanced_tree(root)


def same_tree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1 and root2:
        if root1.data != root2.data:
            return False
        else:
            return same_tree(root1.left,root2.left) and same_tree(root1.right, root2.right)
    
    
root1 = Node(1, Node(1), None)  
root2 = Node(1, Node(2), Node(1))  

same_tree(root1, root2)  



def subtree(root, subroot):
    if not root and not subroot:
        return True
    if not root and subroot:
        return False
    if root and not subroot:
        return True
    if same_tree(root, subroot):
        return True
    return same_tree(root.left, subroot) or same_tree(root.right, subroot)
    
    
root = Node(3, Node(4, Node(1), Node(2, Node(0))), Node(5))
subroot = Node(4, Node(1), Node(2))

subtree(root, subroot)


def level_order_traversal(root):
    from collections import deque
    queue = deque()
    biglist = []
    queue.append(root)
    while queue:
        smalllist = []
        qlen = len(queue)
        for _ in range(qlen):
            popped = queue.popleft()
            if popped:
                smalllist.append(popped.data)
            # root = Node(popped)
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
        biglist.append(smalllist)
                
    return biglist
    
    
root = Node(3)
root.left = Node(9)
root.right = Node(20, Node(15), Node(17))

level_order_traversal(root)


def maximum_path_sum_BT(root):
    res = 0
    def dfs(cur):
        nonlocal res
        if not cur:
            return 0
        
        leftmax = max(0, dfs(cur.left))
        rightmax = max(0, dfs(cur.right))
        
        res = max(res, leftmax + rightmax + cur.data)
        maxm = max(leftmax, rightmax) + cur.data
        return maxm
    dfs(root)
    return res

    
root = Node(-10)
root.left = Node(9)
root.right = Node(20, Node(15), Node(7))

maximum_path_sum_BT(root)


def LCA_BST(root, p, q):
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

p = 2
q = 4
LCA_BST(root, p, q)


def validate_BST(root):
    llist = []
    def inorder(root):
        if not root:
            return True
        inorder(root.left)
        llist.append(root.data)
        inorder(root.right)
        return llist
    inorder(root)    
    return llist == sorted(llist)
    
    
root = Node(2)
root.left = Node(4)
root.right = Node(3)  

validate_BST(root)  


def kth_smallest_BST(root, k):
    llist = []
    def inorder(root):
        if not root:
            return True
        inorder(root.left)
        llist.append(root.data)
        inorder(root.right)
        return llist
    inorder(root)    
    return llist[k-1]
    
root = Node(3)
root.left = Node(1, None, Node(2))
root.right = Node(4) 

k = 3  

kth_smallest_BST(root, k)



def construct_from_preorder_inorder(preorder, inorder):
    if not preorder or inorder:
        return None
    root = Node(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = construct_from_preorder_inorder(preorder[1:mid+1], inorder[:mid])
    root.right = construct_from_preorder_inorder(preorder[mid+1:], inorder[mid+1:])
    return root
    
    
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

construct_from_preorder_inorder(preorder, inorder)



def right_view_BT(root):
    from collections import deque
    queue = deque()
    queue.append(root)
    biglist = []
    while queue:
        if not root:
            return []
        smalllist = []
        for _ in range(len(queue)):
            popped = queue.popleft()
            if popped:
                smalllist.append(popped.data)
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
        biglist.append(smalllist[-1])
    return biglist
        
        
root = Node(1)
root.left = Node(2, None, Node(5))
root.right = Node(3, None, Node(4)) 
    
right_view_BT(root)


###Largest Increasing Subsequence
def LIS(nums):
    n = len(nums)
    dp = [1] * n
    # l, r = 0, 1
    for r in range(1, n):
        for l in range(r):
            if nums[r] > nums[l]:
                dp[r] = max(dp[r], dp[l] + 1)
    return dp[-1]
    
    
    
nums = [10,9,2,5,3,7,101,18]

LIS(nums)


###Largest Common Subsequence
def LCS(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0] * (m+1)] * (n+1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if text2[i-1] == text1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[-1][-1]
    
    
text1 = "abcde"
text2 = "ace" 

LCS(text1, text2)


def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount+1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], 1 + dp[i - c])
    return dp[amount] if dp[amount] != amount + 1 else -1
    
    
coins = [1,2,5]
amount = 11

coin_change(coins, amount)


def house_robber(nums):
    dp = nums.copy()
    dp[0] = nums[0]
    dp[1] = max(dp[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    return dp[-1]
    
    
nums = [2,7,9,3,1]
house_robber(nums)

def house_robber_II(nums):
    n = len(nums)
    dp_start = house_robber(nums[0:n - 1])
    dp_end = house_robber(nums[1:n])
    
    return max(dp_start, dp_end)
    
nums = [1,2,3,1]

house_robber_II(nums)


def jump_game(nums):
    target = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= target:
            target = i
    return True if target == 0 else False
    
    
nums = [3,3,1,0,4]
jump_game(nums)



def unique_paths(m, n):
    dp = [[1] * n] * m
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

m = 3
n = 7

unique_paths(m, n)


def word_break(s, wordDict):
    l, r = 0, 0
    for r in range(len(s)+1):
        for word in wordDict:
            if s[l:r] == word:
                l = r
    return True if l == r else False
    
        
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

word_break(s, wordDict)


def longest_substring_wo_repeat(s):
    l, r = 0, 0
    longest = 1
    charSet = set()
    while r < len(s):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        longest = max(longest, r - l + 1)
        r += 1
    return longest
        
        
s = "pwwkew"   
longest_substring_wo_repeat(s)


def longest_repeating_character_replacement(s, k):
    l, r = 0, 0
    count = {}
    res = 0
    
    while r < len(s):
        if s[r] not in count:
            count[s[r]] = 1
        else:
            count[s[r]] += 1
            
        if (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        else:
            res = max(res, r - l + 1)
        r += 1            
        print(res)
        
    return res
    
s = "AABABBA"
k = 2

longest_repeating_character_replacement(s, k)


def valid_parentheses(s):
    stack = []
    hashMap = {'(':')',
              '{':'}',
              '[':']'}
    for i in s:
        if i in hashMap.keys():
            stack.append(i)
        elif i in hashMap.values():
            popped = stack[-1]
            if i == hashMap[popped]:
                stack.pop()
            
    return True if stack == [] else False
    
    
s = "()[({})]"
valid_parentheses(s)


def combination_sum(candidates, target):
    res = []
    
    def backtrack(i, candidates, target, subset):
        if target == 0:
            res.append(subset.copy())
            
        for i in range(i, len(candidates)):
            subset.append(candidates[i])
            newtarget = target - candidates[i]
            if newtarget >= 0:
                backtrack(i, candidates, newtarget, subset)
            subset.pop()
         
    backtrack(0, candidates, target, [])    
    return res
            
    
        
candidates = [2,3,4,7]
target = 7
combination_sum(candidates, target)


biglist = ['today is a sunny day', 'tomorrow will be a windy day','it is always sunny in New York']

hashMap = {}

for i in range(len(biglist)):
    words = biglist[i].split()
    bigrams = []
    for k in range(len(words) - 1):
        bigram = str(words[k:k+2])
        bigrams.append(bigram)
    for j in range(len(words)):
        if words[j] not in hashMap:
            hashMap[words[j]] = 1
        else:
            hashMap[words[j]] += 1
         
    for l in range(len(words) - 1):
        if bigrams[l] not in hashMap:
            hashMap[bigrams[l]] = 1
        else:
            hashMap[bigrams[l]] += 1
