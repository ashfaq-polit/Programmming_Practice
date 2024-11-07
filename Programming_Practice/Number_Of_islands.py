#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","0","0","0","0"],
  ["0","0","0","0","0"]
]



def dfs(grid, visited, row, col):
    # count = 0
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1' or visited[row][col] == 1:
        return 
    visited[row][col] = 1

    dfs(grid, visited, row + 1, col)
    # print(row)
    dfs(grid, visited, row, col + 1)
    dfs(grid, visited, row - 1, col)
    dfs(grid, visited, row, col - 1)
    # return count

def adjacent_1s(grid):
    num_row, num_col = len(grid), len(grid[0])
    visited = [[0] * num_col for _ in range(num_row)]
    
    count = 0
    
    for row in range(num_row):
        for col in range(num_col):
            if grid[row][col] == '1' and not visited[row][col]:
                dfs(grid, visited, row, col)
                count += 1
    
    return count
    
            
adjacent_1s(grid)        





