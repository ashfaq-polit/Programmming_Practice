#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""


def contains_duplicate(nums):
    hash_map = {}
    for i in nums:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            return True
    return False

nums = [1, 2, 3, 3]        
contains_duplicate(nums)



def valid_anagram(s, t):
    hash_mapS = {}
        
    for i in s:
        if i not in hash_mapS:
            hash_mapS[i] = 1
        else:
            hash_mapS[i] += 1
            
    for j in t:
        if j not in hash_mapS:
            return False
        else:
            hash_mapS[j] -= 1
            
    return all(value == 0 for value in hash_mapS.values())
        
s = "racecar"
t = "carrace"

valid_anagram(s, t)



def Two_sum(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff not in hash_map:
            hash_map[nums[i]] = i
        else:
            return [hash_map[diff], i]
        
       
nums = [5, 5]
target = 10

Two_sum(nums, target)



def group_anagrams(strs):
    from collections import defaultdict
    res = defaultdict(list)
    
    
    for s in strs:
        count = [0]*26
        for c in s:
            if c not in count:
                count[ord(c) - ord("a")] = 1
            else:
                count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return res.values()
            
                
strs = ["act","pots","tops","cat","stop","hat"]

group_anagrams(strs)



def top_k_frequent_element(nums, k):
    freq = [[] for i in range(len(nums) + 1)]
    hash_map = {}
    
    for i in nums:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1
            
    for n, c in hash_map.items():
        freq[c].append(n)
        
    res = []
    for j in range(len(freq) - 1, 0, -1):
        for n in freq[j]:
            res.append(n)
            if len(res) == k:
                return res

        
nums = [1,2,2,3,3,3]
k = 2

top_k_frequent_element(nums, k)



def product_of_array_except_self(nums):
    left_prod = [1] * len(nums)
    right_prod = [1] * len(nums)
    prod = [1] * len(nums)
    
    for i in range(1, len(nums)):
        left_prod[i] = left_prod[i - 1] * nums[i - 1]
        
    print(left_prod)
        
    for j in range(len(nums) - 2, -1, -1):
        right_prod[j] = right_prod[j + 1] * nums[j + 1]
        
    for k in range(len(nums)):
        prod[k] = left_prod[k] * right_prod[k]
    
    return prod
    
nums = [2,1,4,6]

product_of_array_except_self(nums)



def two_sum_II(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            return [l, r]
    
    
numbers = [1,2,3,4]
target = 3

two_sum_II(numbers, target)



def three_sum(nums):
    nums.sort()
    # l, r = 0, len(nums) - 1
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        else:
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
            print(res)
    
    return res
        
nums = []

three_sum(nums)


def max_water_container(height):
    l, r = 0, len(height) - 1
    max_capacity = float('-inf')
    while l < r:
        capacity = (r - l) * min(height[l], height[r])
        max_capacity = max(capacity, max_capacity)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_capacity
    
    
height = [2,2,2]

max_water_container(height)




def Happy_number(n):
    sumsquare_set = set()

    while n not in sumsquare_set:
        sumsquare_set.add(n)
        n = find_sumsquare(n) 
        print(n)      
        if n == 1:
            return True
    return False
            

def find_sumsquare(n):
    rem = []
    while n > 0:
        m = n % 10
        n = n // 10
        rem.append(m)
        
    sumsquare = 0
     
    for i in rem:
         sumsquare += i*i
    return sumsquare        
               
n = 101

Happy_number(n)



def plus_one(digits):
    digit = 0
    final_list = []
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] + 1 < 10:
            digits[i] = digits[i] + 1
            return digits
        else:
            digits[i] = 0
            
    if not digits[0]:
        digits.append(1)
        return digits[::-1]
    

digits = [9,9,9,9]

plus_one(digits)



def spiral_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    L = 0
    R = cols
    T = 0
    B = rows
    
    spiral_list = []
    
    while L < R and T < B:
        
        for i in range(L, R):
            spiral_list.append(matrix[T][i])
        T += 1
        
        for j in range(T, B):
            spiral_list.append(matrix[j][R - 1])
        R -= 1
        
        if not (L < R and T < B):
            break
       
        for k in reversed(range(L, R)):
            spiral_list.append(matrix[B - 1][k])
        B -= 1
        
        for l in reversed(range(T, B)):
            spiral_list.append(matrix[l][L])
        L += 1
        
    return spiral_list
    
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

spiral_matrix(matrix)


def set_matrix_zeros(matrix):
    import numpy as np
    
    ## Using copy matrix
    # copy = np.array(matrix).copy()
    
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         if matrix[i][j] == 0:
    #             copy[i, :] = 0
    #             copy[:, j] = 0
    # return copy
    
    ## Using extra row and column
    # rows = [1] * len(matrix)
    # cols = [1] * len(matrix[0])
    
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         if matrix[i][j] == 0: 
    #             rows[i] = 0
    #             cols[j] = 0
                
    # matrix = np.array(matrix)
    
    # for i in range(len(rows)):
    #     for j in range(len(cols)):
    #         if rows[i] == 0:
    #             matrix[i, :] = 0
    #         if cols[j] == 0:
    #              matrix[:, j] = 0
                
    # return matrix

    matrix = np.array(matrix)
    
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0 
                matrix[i][0] = 0
            
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0 
            else:
                continue

    for i in range(0, 1):
        for j in range(0, 1):
            if matrix[i][j] == 0:
                matrix[0, :] = 0
                matrix[:, 0] = 0
                
    return matrix
                
        
    
matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]    
set_matrix_zeros(matrix)   



def rotate_image(matrix):
    L, R = 0, len(matrix) - 1
    T, B = L, R
    while L < R:
        for i in range(L, R):
            temp = matrix[T][L+i] 
            matrix[T][L+i] = matrix[B-i][L]
            matrix[B-i][L] = matrix[B][R-i]
            matrix[B][R-i] = matrix[T+i][R]
            matrix[T+i][R] = temp
            
            L += 1
            R -= 1
    return matrix
            
       
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

rotate_image(matrix)


def GCD_2numbers(num1, num2):
    if num2 > num1:
        num1, mum2 = num2, num1
        
    while num2 > 0:
        rem = num1 % num2
        num1 = num2
        num2 = rem
        
    return num1
        
            
num1 = 70
num2 = 15

GCD_2numbers(num1, num2)


def compress_characters(string):
    hash_map = {}
    for i in range(0, len(string) - 1, 2):
        if string[i] not in hash_map:
            hash_map[string[i]] = int(string[i+1])
        else:
            hash_map[string[i]] += int(string[i+1])
            
    output = ""
            
    for key in hash_map:
        output += key
        output += str(hash_map[key])
        
    return output

   
string = "a3b2c5a7g9c2"

compress_characters(string)



def decimal_to_binary(num):
    string = ''
    while num > 0:
        rem = num % 2
        num = num // 2
        string += str(rem)
        
    return int(string[::-1])
        
       
num = 37

decimal_to_binary(num)



def Fibonacci_triangle(n):
    for i in range(n + 1):
        a = 0
        b = 1
        line = []
        for j in range(i):
            c = a + b
            line.append(str(b))
            a = b
            b = c
        print("\t".join(line))
            
n = 5

Fibonacci_triangle(n)


def count_1bits(num):
    count = 0
    while num > 0:
        rem = num % 2
        if rem == 1:
            count += 1
        num = num // 2
    return count
            
        
num = 23
count_1bits(num)


def single_number(nums):
    res = 0
    for i in nums:
        res = res ^ i
    return res
    
    
nums = [7,6,6,7,8]
    
single_number(nums)


def password_decoding(password):
    password = str(password)
    output = ''
    i = 0
    while i < len(password) - 1:
        temp = int(password[i] + password[i+1])
        if temp == 32:
            output += ' '
            i += 2
        elif temp in range(65, 100):
            output += chr(temp)
            i += 2
        elif i + 2 < len(password):
            temp = int(password[i] + password[i+1] + password[i+2])
            output += chr(temp)
            i += 3
    return str(output)
        
            
password = 801141011273110115  
  
password_decoding(password)    



def find_monsters(string):
    minimum = float('inf')
    groups = string.split("@")
    

    for i in range(len(groups)):
        group = groups[i].split("$")
        print(len(min(group)))
        minimum = min(minimum, len(min(group)))
            
    return minimum
        
           
string = "PPPPPP@PPP@PPP$PP"

find_monsters(string)


def strong_password(password):
    
    lowercase, uppercase, digit, special  = False, False, False, False
    
    for c in password:
        if c.islower():
            lowercase = True
        elif c.isupper():
            uppercase = True
        elif c.isdigit():
            digit = True
        elif c in ('!@#$%^&*()-+'):
            special = True
        elif c == c + 1:
            return False
        
    return lowercase and uppercase and digit and special and len(password) >= 8
            
            
password = "1aB!"

strong_password(password)



def to_alternate_uppercase(string):
    count = 1
    output = []
    for i in range(len(string)):
        if string[i].isalpha():
            count += 1
            if count % 2 == 0:
                output.append(string[i].upper())
            else:
                output.append(string[i])
        else:
            output.append(string[i])
                
    return ''.join(output)
            
            
string = "We are the world"

to_alternate_uppercase(string)


def maximum_subarray(nums):
    total, largest = 0, nums[0]
    l, r = 0, 0
    for r in nums:
        total += r
        largest = max(largest, total)
        if total < 0:
            l = r + 1
            total = 0
    return largest
    

nums = [-2,1,-3,4,-1,2,1,-5,4]

maximum_subarray(nums)


def sort_colors(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] < nums[i]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums
    
    
nums = [2,0,2,1,1,0]

sort_colors(nums)


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
def insert_doubly_linked_list_begin(root, data):
    newNode = Node(data)
    newNode.next = root
    root.prev = newNode
    return newNode
    
def insert_doubly_linked_list_end(root, data):
    newNode = Node(data)
    cur = root
    while cur and cur.next:
        cur = cur.next
    cur.next = newNode
    newNode.prev = cur
    return root
    
    
root = Node(1)
l1 = Node(2)
l2 = Node(3)

root.next = l1
l1.next = l2

l1.prev = root
l2.prev = l1


insert_doubly_linked_list_begin(root, 0)
insert_doubly_linked_list_end(root, 0)



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
def validate_BST(root):
    llist = []
    def inorder_traversal(root):
        if not root:
            return 
        inorder_traversal(root.left)
        llist.append(root.data)
        inorder_traversal(root.right)
        return llist
    
    return inorder_traversal(root) == sorted(llist) 
    
        
    
root = Node(2)
root.left = Node(1)
root.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(6)

validate_BST(root)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def cycle_linked_list(root):
    l, r = root, root
    while r and r.next:
        l = l.next
        r = r.next.next
        if l == r:
            return True
    return False
        
                
root = Node(3)
root.next = Node(4)
root.next.next = Node(5)
root.next.next.next = Node(6)
root.next.next.next.next = root.next

cycle_linked_list(root)  


def reverse_linked_list(root):  
    prev, cur = None, root
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
           
root = Node(3)
root.next = Node(4)
root.next.next = Node(5)
root.next.next.next = Node(6)

reverse_linked_list(root)



def kth_largest_element_array(nums):
    n = len(nums)
    p = n - 1 #pivot
    l = 0
    def quick_select(l, p):
        while l < p :
            if nums[l] < nums[p]:
                l += 1
        nums[l], nums[p] = nums[p], nums[l]
       
        if l == n - k:
            return nums[l]
        elif l > n - k:
            quick_select(n - k, p)
        else:
            quick_select(l, p)
            

nums = [2,3,1,1,5,5,4]
k = 3    

kth_largest_element_array(nums)



def factorial(n):
    if n == 1:
        return 1
    # else:
    #     res = 1
    #     for i in range(1, n + 1):
    #         res *= i
    #     return res
    return n * factorial(n - 1)
        
factorial(5)


class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
def LCA_BST(root, p, q):
    if not root or root == p or root == q:
        return root
    while root:
        if p < root.data and q < root.data:
            root = root.left
        elif p > root.data and q > root.data:
            root = root.right
        else:
            return root.data
           
            
root = Node(5)
root.left = Node(3, Node(1, None, Node(2)), Node(4))
root.right = Node(8, Node(7), Node(9))
    
p = 5
q = 4

LCA_BST(root, p, q)   


def balanced_binary_tree(root):
    
    def height(root):
        if not root:
            return 0
        return 1 + max(height(root.left), height(root.right))
    
    return abs(height(root.left) - height(root.right)) <= 1
            
    
root = Node(1)
root.left = Node(2)
root.right = Node(3, Node(4, Node(5), None), None)

balanced_binary_tree(root)


### IBM interview question
def game_winner(s):
    def remove_middle_char(s, char):
        # Look for sequences of 'www' or 'bbb' and remove the middle character
        target = char * 3
        while target in s:
            s = s.replace(target, char + ' ' + char, 1)  # Remove the middle character by replacing
        return s.replace(' ', '')  # Remove spaces after all replacements

    # Game loop
    while True:
        # Wendy's turn
        new_s = remove_middle_char(s, 'w')
        if new_s == s:
            return 'Bob'  # If Wendy has no move, Bob wins
        s = new_s

        # Bob's turn
        new_s = remove_middle_char(s, 'b')
        if new_s == s:
            return 'Wendy'  # If Bob has no move, Wendy wins
        s = new_s

# Example usage
string = "wwwbbbwwwwwbb"
game_winner(string) # Expected output: Depends on the game progression


