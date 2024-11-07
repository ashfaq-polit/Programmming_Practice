#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

grid =    [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]



def dfs(grid, row, col, prevVal, ocean):
    # count = 0
    if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or ocean[row][col] == 1 \
    or grid[row][col] < prevVal: 
        return 
    ocean[row][col] = 1

    dfs(grid, row + 1, col, grid[row][col], ocean)
    dfs(grid, row, col + 1, grid[row][col], ocean)
    dfs(grid, row - 1, col, grid[row][col], ocean)
    dfs(grid, row, col - 1, grid[row][col], ocean)


def pacific_atlantic(grid):
    num_row, num_col = len(grid), len(grid[0])
    pacific = [[0] * num_col for _ in range(num_row)]
    atlantic = [[0] * num_col for _ in range(num_row)]
    
####Pacific Ocean
    for col in range(num_col):
        dfs(grid, 0, col, grid[0][col], pacific)
        dfs(grid, num_row - 1, col, grid[num_row - 1][col], atlantic)
    
    for row in range(num_row):
        dfs(grid, row, 0, grid[row][0], pacific)
        dfs(grid, row, num_col - 1, grid[row][num_col - 1], atlantic)
        
    res = []
    for i in range(num_row):
        for j in range(num_col):
            if pacific[i][j] == 1 and atlantic[i][j] == 1:
                res.append([i, j])
                
    return res
    #return pacific, atlantic, pacific[0][0]
    
            
pacific_atlantic(grid) 