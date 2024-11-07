#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

def Subsets(nums):
   res  = [] 
   cur = []     
   def backtrack(i):
       if i == len(nums):
           res.append(cur.copy())
           # print(res)
           return

       # return
          
       # for i in range(i, len(nums)-1):
       # print(cur)
       cur.append(nums[i])  
       #print(i)         
       backtrack(i+1)
       cur.pop()
       print(cur)
       # print('i:', i)
       backtrack(i+1)
         
   backtrack(0)
   return res

def Subsets(nums):
   res  = [] 
   cur = []     
   def backtrack(i):
       if i == len(nums):
           res.append(cur.copy())
           # print(res)
           return

       # return
          
       for i in range(i, len(nums)-1):
       # print(cur)
           cur.append(nums[i])  
       #print(i)         
           backtrack(i+1)
           cur.pop()
       #print(cur)
       # print('i:', i)
           backtrack(i+1)
         
   backtrack(0)
   return res
  
      
nums = [1,2,3]
Subsets(nums) 

###https://www.physicsforums.com/threads/finding-all-subsets-of-a-list-of-positive-integers-using-backtracking.1011464/
alist = [1,2,3] 
ans = [] 
def backtrack(nums, start, curr): 
    ans.append(curr) 
    for i in range(start, len(nums)): 
        backtrack(nums, i+1, curr + [nums[i]]) 
        
def subsets(nums): 
    backtrack(nums, 0, []) 
    return ans 

print(subsets(alist))





def permutations_recursive(nums):
    if len(nums) == 1:
        return [nums]
    
    result = []
    for i in range(len(nums)):
        current_num = nums[i]
        print('current_num:',current_num)
        remaining_nums = nums[:i] + nums[i+1:]
        print('remaining_nums:',remaining_nums)
        sub_permutations = permutations_recursive(remaining_nums)
        print('sub_permutations:', sub_permutations)
        
        for perm in sub_permutations:
            result.append([current_num] + perm)
            print('result:', result)
    
    return result

# Example usage
nums = [1, 2, 3]
result_recursive = permutations_recursive(nums)
print("Permutations (Recursive):", result_recursive)




def calcSubset(A, res, subset, index):
	# Add the current subset to the result list
	res.append(subset.copy())

	# Generate subsets by recursively including and excluding elements
	for i in range(index, len(A)):
		# Include the current element in the subset
		subset.append(A[i])
		# Recursively generate subsets with the current element included
		calcSubset(A, res, subset, i + 1)

		# Exclude the current element from the subset (backtracking)
		subset.pop()


def subsets(A):
	subset = []
	res = []
	index = 0
	calcSubset(A, res, subset, index)
	return res


array = [1, 2, 3]
subsets(array)


