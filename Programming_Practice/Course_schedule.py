#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['C']
}

numCourses = 2
prerequisites = [[1,0],[0,1]]

graph = {}

for sublist in prerequisites:
    first_no = sublist[0]
    second_no = sublist[1]
    if first_no in graph:
        if isinstance(graph[first_no], list):
            graph[first_no].append(second_no)
        graph[first_no] = [graph[first_no], second_no]
    else:
        graph[first_no] = [second_no]

            

def dfs(graph, node, visited = None, path = None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
        
    visited.add(node)
    print(node)
    
    path.append(node)
    print(path)
        
    for neighbor in graph.get(node):
        if neighbor in path:
            print('Cycle detected')
            return True
        elif neighbor not in visited:
            if dfs(graph, neighbor, visited, path):
                return True
            
    path.pop()
    return False

               
dfs(graph, list(graph.keys())[0])       

    
            
    
    

