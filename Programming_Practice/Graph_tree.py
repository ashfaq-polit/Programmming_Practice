#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

###Flood Fill
def flood_fill(image, sr, sc, color):
    if image[sr][sc] == color:
        return image
    else:
        source = image[sr][sc]
        fill(image, sr, sc, source, color)
        return image
    
def fill(image, sr, sc, source, color):
    if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != source:
        return
    else:
        image[sr][sc] = color
        fill(image, sr-1, sc, source, color)
        fill(image, sr+1, sc, source, color)
        fill(image, sr, sc-1, source, color)
        fill(image, sr, sc+1, source, color)
        
    
    
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]

sr = 1
sc = 1
color = 2

flood_fill(image, sr, sc, color)





###Course Schedule
#https://www.youtube.com/watch?v=EUDwWbvtB_Q&t=480s
from collections import deque, defaultdict

def course_schedule(numCourses, prerequisites):
    indegree = [0] * numCourses
    graph = [[] for _ in range(numCourses)]
    
    for crs, pre in prerequisites:
        graph[pre].append(crs)
        indegree[crs] += 1
        
    queue = []
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)
            
    
    visited = 0
    while queue:
        node = queue.pop(0)
        print(node)
        visited += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            print(indegree)
            if indegree[neighbor] == 0:
                queue.append(neighbor)
            
    
    return numCourses == visited
    
    
        
numCourses = 3
prerequisites = [[1,0], [0,1], [0,2]]

course_schedule(numCourses, prerequisites)



###Number of Islands
#https://www.youtube.com/watch?v=o8S2bO3pmO4
def No_of_Island(grid):
    if not grid:
        return 0
    count = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += dfs(grid, i, j)
    return count
  
def dfs(grid, i ,j):
    if i < 0 or j < 0 or i >=len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
        return 0
    else:
        grid[i][j] = "0"
        dfs(grid, i-1, j)
        dfs(grid, i+1, j)
        dfs(grid, i, j-1)
        dfs(grid, i, j+1)
        
    return 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

No_of_Island(grid)



###Rotten Oranges
def rotten_oranges(grid):
    from collections import deque
    fresh, rotten = 0, 0
    queue = deque()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                rotten += 1
                queue.append([r, c])
    
    directions = [[-1,0], [1,0], [0,1], [0,-1]]
    while queue and fresh > 0:
        for i in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1):
                    continue
                elif grid[row][col] == 1:
                    grid[row][col] = 2
                    queue.append([row,col])
                    fresh -= 1
        count += 1
    return count if fresh == 0 else -1 
                    
grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]
             
rotten_oranges(grid)      


### Word Search
def word_search(board, word):
    path = set()
    
    def dfs(i, j, count):
        if count == len(word):
            return True
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or board[i][j] != word[count] or (i,j) in path:
            return False
        else:
            path.add((i, j))
            print(path)
            found = (dfs(i-1, j, count+1) or dfs(i+1, j, count+1) or dfs(i, j-1, count+1) or dfs(i, j+1, count+1))
            path.remove((i, j))
            print("path:",path)
            return found 
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False
            


board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "SEE"    
        
word_search(board, word) 