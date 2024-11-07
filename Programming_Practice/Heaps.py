#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

###K closest points to origin
import heapq
points = [[3,3],[5,-1],[-2,4]]
k = 2

def k_closest_points(points, k):
    minHeap = []
    for (x, y) in points:
        dist = x ** 2 + y ** 2
        minHeap.append([dist, x, y])
       
    heapq.heapify(minHeap)
    
    res = []
    while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x, y])
        k -= 1
    return res

k_closest_points(points, k)


###Top K Frequent Elements
nums = [1,1,1,2,2,3]
k = 2

def top_k_frequent_elements(nums, k):
    heapmap = {}
    for i in nums:
        if i not in heapmap:
            heapmap[i] = 1
        else:
            heapmap[i] += 1
            
    heap_list = [(value, key) for key, value in heapmap.items()]
    heapq.heapify(heap_list)
    
    print(heap_list)
    
    res = []
    n = len(heapmap) 
    while n - k > 0:
        heapq.heappop(heap_list)
        n -= 1
        
    while k > 0:
        x, y = heapq.heappop(heap_list)
        res.append(y)
        k -= 1
        
    return res

top_k_frequent_elements(nums, k)
        

###Median from data Stream
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        

    def addNum(self, num):
        heapq.heappush(self.small, -1 * num)
        
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
            
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
            
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        
        return self.small, self.large

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        if len(self.small) < len(self.large):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2
    
    
medianFinder = MedianFinder()
medianFinder.addNum(1)    
medianFinder.addNum(2)   
medianFinder.findMedian() 
medianFinder.addNum(3)   
medianFinder.findMedian()




###Ransom Note
ransomNote = "aa"
magazine = "aab"

def ransom_note(ransomNote, magazine):
    hash_map = {}
    for i in magazine:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1
            
    
    for i in ransomNote:
        if i in hash_map and hash_map[i] > 0:
            hash_map[i] -= 1
        else:
            return False
    return True    

ransom_note(ransomNote, magazine)
    
