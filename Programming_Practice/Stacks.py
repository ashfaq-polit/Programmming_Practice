#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

###Valid parentheses
s = "[()]"

def valid_parentheses(s):
    dict = {'(':')',
            '{':'}',
            '[':']'}
    
    stack = []
    
    for i in s:
        if i in dict.keys():
            stack.append(i)
        elif i != dict[stack[-1]]:
            return False
        else:
            stack.pop()

    return True if not stack else False
            
                
valid_parentheses(s)    


###Queue using Stack

class MyQueue(object):

    def __init__(self):
       self.s1 = []
       self.s2 = []
        
    def push(self, x):
        self.s1.append(x)
        

    def pop(self):
        if not self.s2:
            while self.s1:
                x = self.s1.pop()
                self.s2.append(x)
        return self.s2.pop()
                
        

    def peek(self):
        if not self.s2:
            while self.s1:
                x = self.s1.pop()
                self.s2.append(x)
        return self.s2[-1]
        

    def empty(self):
        return max(len(self.s1), len(self.s2)) == 0
        
myQueue = MyQueue();
myQueue.push(1)
myQueue.push(2)
myQueue.peek()
myQueue.pop()
myQueue.empty()


###Reverse Polish Notation
tokens =  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

def reverse_polish_notation(tokens):
    stack = []
    res = 0
    for i in tokens:
        if i in ('+-*/'):
            x = int(stack.pop())
            y = int(stack.pop())
            if i == '+':
                res = x + y
            elif i == '-':
                 res = y - x
            elif i == '*':
                 res = x * y
            elif i == '/':
                 res = int(y / x)
            stack.append(res)
            print(res)
        else:
            stack.append(i)
            print(stack)
    return res
        
reverse_polish_notation(tokens)   


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minm = float('inf')
        

    def push(self, val):
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
            self.minm = val
        else:
            self.minm = min(val, self.minm)
            self.minStack.append(self.minm)
        print(self.minm)
        

    def pop(self):
        self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minStack[-1]
            
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(3)
param_2 = obj.getMin()        
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()        



###Trapping rain water
height = [4,2,0,3,2,5]
n = len(height) - 1
left_max = [0] * n
right_max = [0] * n
trapped = [0] * n

for i in range(1, len(height) - 1):
    left_max[i] = max(height[:i])
    right_max[i] = max(height[i:])
    trapped[i] = max(0, (min(left_max[i], right_max[i]) - height[i]))
print(sum(trapped))