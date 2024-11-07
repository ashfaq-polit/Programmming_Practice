#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

arr = [-1, 0, 3, 5, 9, 12]

target = 10


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right ) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False 
  
binary_search(arr, target)



##Remove duplicates
nums = [0,0,1,1,1,2,2,3,3,4]
import numpy as np

def remove_duplicates(nums):
    l, r = 0, 0
    for r in range(1, len(nums)):
        if nums[l] == nums[r]:
            nums[r] = np.nan
        else:
            l += 1
            nums[l] = nums[r]
    return l, nums
            
remove_duplicates(nums)


### Squares of a Sorted Array
nums = [-4,-1,0,3,10]

def squares_sorted(nums):
    l = 0
    r = len(nums) - 1
    ans = []
    

    while l <= r:
        if abs(nums[l]) < abs(nums[r]):
            ans.append(nums[r] * nums[r])
            r -= 1
        else:
            ans.append(nums[l] * nums[l])
            l += 1
            
    return ans[::-1]


squares_sorted(nums)


        
        
###Majority Element        
nums = [2,2,1,1,1,2,2]

def majority_element(nums):
    dict = {}
    
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
        if dict[i] > len(nums) // 2:
            return i
        
majority_element(nums)

##Moore's solution
def majority_element(nums):
    count, res = 0, nums[0]
    for i in nums:
        if count == 0:
            res = i
        if i == res:
            count += 1
        else:
            count -= 1
                
    return res, count
        
majority_element(nums)


###Maximum Subarray
nums = [-2,1,-3,4,-1,2,1,-5,4]

def Maximum_Subarray(nums):
    import numpy as np
    maxm, l, total = -np.inf, 0, 0
    
    for r in range(len(nums)):
        total += nums[r]
        maxm = max(maxm, total)
        print(maxm)
        if total < 0: 
            total = 0
            l = r + 1
    return maxm
    
Maximum_Subarray(nums)


###Power
x = 2
n = 3

def Power_xn(x, n):
    ans = 1
    if x == 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return x
    else:
        for i in range(abs(n)):
            ans = ans * x 
        return ans if n > 0 else 1/ans
        
Power_xn(x, n)


###Smaller Numbers After Self
nums = [5,2,6,1]

def smaller_no_after_self(nums):
    ans = []
    for i in range(len(nums)):
        count  = 0
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                count += 1
        # print(i, count)
        ans.append(count)
    return ans

smaller_no_after_self(nums)



###Find K Closest Elements
arr = [1,2,3,4,5]
k = 4
x = 3

def k_closest_elements(arr):
    l, r = 0, len(arr) - k
    
    while l < r:
        mid = (l + r) // 2
        if abs(arr[mid] - x) > abs(arr[mid+k] - x):
            l = mid + 1
        else:
            r = mid
        print(mid, l, r)
    return arr[l:l+k]
            
k_closest_elements(arr)     



###Remove element
nums = [0,1,2,2,3,0,4,2]
val = 2     
                
def remove_element(nums):
    l, r = 0, 0
    for r in range(len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1
    return l, nums
            
remove_element(nums)      



###3Sum
nums = [0,0,0] 

def threesum(nums):
    nums = sorted(nums)
    res = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        else:
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
    return res
                
threesum(nums)   



###Container With Most Water
height = [1,8,6,2,5,4,8,3,7] 

def container_most_water(height):
    l, r, maxm = 0, len(height) - 1, 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        maxm = max(area, maxm)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxm
    
container_most_water(height)   
    


###Trapping Rain Water
height = [0,1,0,2,1,0,1,3,2,1,2,1]

left_max = [0 for _ in range(len(height))]
right_max = [0 for _ in range(len(height))]
min_left_right = [0 for _ in range(len(height))]
trapped = [0 for _ in range(len(height))]
total = 0

for i in range(1, len(height)):
    left_max[i] = max(height[i], left_max[i - 1])
    
for j in range(len(height)-2, -1, -1):
    right_max[j] = max(height[j], right_max[j + 1])
    
for k in range(len(height)):
    min_left_right[k] = min(left_max[k], right_max[k])
    trapped[k] = max(0, min_left_right[k] - height[k])
    total += trapped[k]

print('total:', total)

def trapping_rain_water(height):
    l, r = 0, len(height) - 1
    maxLeft, maxRight = height[l], height[r]
    trapped = 0
    
    while l < r:
        if maxLeft <= maxRight:
            l += 1
            maxLeft = max(maxLeft, height[l])
            trapped += max(0, min(maxLeft, maxRight) - height[l])
        else:
            r -= 1
            maxRight = max(maxRight, height[r])
            trapped += max(0, min(maxLeft, maxRight) - height[r])
        print(trapped)   
    return trapped
        
trapping_rain_water(height)       
        
        
    

    