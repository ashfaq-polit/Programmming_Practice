#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

Stack = [1, 2, 4, 6, 7, 4, 9, 7]

popped = Stack.pop()

print(popped)

print(Stack)


class Stack():
    def __init__(self):
        self = []
    def push (self,element):
        self.append(element)
    def pop(self):
        if len(self.Stack > 0):
            self.pop()
        else:
            return
            
        
my_stack = Stack()

my_stack.push(str(3))
my_stack.push(str(4))
my_stack.push(str(8))
my_stack.push(5)

my_stack.pop()

print(str(my_stack))



# Creating a stack
def create_stack():
    stack = []
    return stack


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if len(stack) == 0:
        return "stack is empty"

    return stack.pop()

# Checking valid parethesis
def check_valid_parenthesis(stack):
    if len(stack) == 0:
        return "stack is empty"
    else:
        while len(stack) >1:
            if (stack[-1] == ')' and stack[-2] == '(')\
            or (stack[-1] == '}' and stack[-2] == '{')\
            or (stack[-1] == ']' and stack[-2] == '['):
                stack.pop(), stack.pop()
            else: 
                return

        
stack = create_stack()
push(stack, '(')
push(stack, ')')
push(stack, '[')
push(stack, ']')
push(stack, '{')
push(stack, '}')
print("popped item: " + str(pop(stack)))
print("stack after popping an element: " + str(stack))

check_valid_parenthesis(stack)
if len(stack) == 0:
    print("Valid parenthesis")
else:
    print("Invalid parenthesis")

