#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

arr = [2, 3, 5, 8, 6]


def max_salary(arr):
    salary = ''

    while arr:
        salary += str(max(arr))
        arr.remove(max(arr))
    return int(salary)
    

max_salary(arr)



####Coin change
coins = [1,2,5]
amount = 11

def coin_change(coins, amount):
    change = 0
    coins = sorted(coins, reverse = True)
    
    for i in coins:
        while amount - i >= 0:
            amount -= i
            change += 1
    return change if amount == 0 else -1


coin_change(coins, amount)


#####Maximum units on a truck
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
    
def units_on_truck(boxTypes, truckSize):
    
    total = 0

    boxTypes = sorted(boxTypes, key = lambda x:x[1], reverse = True)
    no_of_boxes = [sublist[0] for sublist in boxTypes]
    units = [sublist[1] for sublist in boxTypes]
    
    # print(no_of_boxes, units)
    
    while truckSize > 0:
        for i in range(len(no_of_boxes)):
            if truckSize - no_of_boxes[i] > 0:
                total += no_of_boxes[i] * units[i]
                # print(total)
                truckSize -= no_of_boxes[i]
                # print(truckSize)
            else:
                total += truckSize * units[i]
                truckSize -= truckSize
    return total
        
units_on_truck(boxTypes, truckSize)   
        
    
#####Jump game
nums = [3,2,1,0,4]
# [2,3,1,1,4]

def jump_game(nums):
    target = len(nums) - 1
    new_target = target - 1
    
    
    # i=0
    # while i < len(nums) - 1:
    #     if nums[i]:
    #         i += nums[i]
                    
    # return True if i >= len(nums) - 1 else False
    
    while target > 0 and new_target >= 0:
        if nums[new_target] >= target - new_target:
            target = new_target
        # else:
        #     target = target
        print(target, new_target)
        new_target -= 1
    return True if target == 0 else False

jump_game(nums)   


####Gas station
gas = [2,3,4]
cost = [3,4,3]

def gas_station(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    else:
        total, l  = 0, 0 
        for r in range(len(gas)):
            supply = gas[r] - cost[r]
            if supply < 0:
                total = 0
                l = r + 1
            else:
                total += supply
        return l 
            
gas_station(gas, cost)   


####Merge Intervals
intervals = [[1,4],[4,5]]

def merge_intervals(intervals):
    # intervals = intervals.append(intervals[-1].copy())
    intervals = sorted(intervals, key = lambda x:x[0], reverse = False)
    res = [intervals[0]]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] <= res[-1][1]:
            # res[-1][0] = intervals[i][0]
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])
        print(i, intervals)   
    return res

merge_intervals(intervals)   


###Insert intervals
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]  

def insert_intervals(intervals, newInterval):
    intervals.append(newInterval)
    
    intervals = sorted(intervals, key = lambda x:x[0], reverse = False)
    
    res = [intervals[0]]
    
    for i in range(1, len(intervals)):
        if res[-1][1] >= intervals[i][0]:
            # res[-1][0] = intervals[i][0]
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])
    return res

def insert_intervals(intervals, newInterval):
    
    intervals = sorted(intervals, key = lambda x:x[0], reverse = False)
    
    # res = [intervals[0]]
    res = []
    
    for i in range(len(intervals)):
        if intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
        elif intervals[i][0] > newInterval[1]:
            res.append(newInterval)
            return res + intervals[i:]
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
        # res.append(newInterval)
    return res
    
insert_intervals(intervals, newInterval) 


points = [[1,2],[2,3],[3,4],[4,5]]

def ballon_burst(points):
    count = len(points)
    points = sorted(points, key = lambda x:x[0], reverse = False)
    
    for i in range(len(points) - 1):
        if points[i][1] >= points[i+1][0]:
            points[i+1][1] = points[i][1]
            count -= 1
    return count
  

ballon_burst(points)  



intervals = [[1,2],[2,3]]

def non_overlapping_interval(intervals):
    intervals = sorted(intervals, key = lambda x:x[0], reverse = False)
    prev, count = 0, 0
    for new in range(1, len(intervals)):
        if intervals[new][0] < intervals[prev][1]:
            count += 1
        else:
            prev += 1
        new += 1
    return count
    
non_overlapping_interval(intervals)


g = [1,2,3] #greed factor
s = [1,1,2] #size

def assign_cookies(g, s):
    g.sort()
    s.sort()
    count, left, i = 0, 0, 0
    while left < len(g) and i < len(s):
        if s[i] >= g[left]:
            count += 1
            left += 1
        i += 1
    return count

assign_cookies(g, s)


###Lemonade Change
bills =  [5,5,5,10,20]
# [5,5,10,10,20]

def lemonade_change(bills):
    fives, tens = 0, 0
    for i in range(len(bills)):
        if bills[i] == 5:
            fives += 1
        elif bills[i] == 10:
            tens += 1
            fives -= 1
        elif tens > 0:
            tens -= 1
            fives -= 1
        else:
            fives -= 3
        if fives < 0:
            return False
    return True
        
lemonade_change(bills)


###Queue-reconstruction-by-height
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
#https://www.youtube.com/watch?v=HKHkzKvb0J4
def queue_by_height(people):
    people = sorted(people, key = lambda x:x[0], reverse=True) 
    print(people)
    ans = []
    
    for i in people:
        ans.insert(i[1], i)
        print(ans)
            
    return ans 

queue_by_height(people)


###Jump Game II
nums = [2,3,1,1,4]

def jump_game2(nums) :
    l, r, furthest = 0, 0, 0
    count = 0
    while r < len(nums) - 1:
        for i in range(l, r+1):
            furthest = max(furthest, i+nums[i])         
        l = r + 1
        r = furthest
        count += 1
    return count
    
jump_game2(nums)       


###Candy distribution
ratings = [5,4,3,5,6,2]

def candy(ratings):
    candy = [1 for _ in range(len(ratings))]
    total = 0
    
    for i in range(len(ratings)-1):
        if ratings[i+1] > ratings[i]:
            candy[i+1] = candy[i] + 1
    print(candy)
    for i in range(len(ratings)-2, -1, -1):
        if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
            candy[i] = candy[i+1] + 1
    print(candy)    
    return sum(candy)
        
candy(ratings)           

        
    