#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""
    
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
            
    def push(self, x):
        self.stack1.append(x)
            
    def pop(self):
        while len(self.stack1) != 0:
            popped = self.stack1.pop()
            self.stack2.append(popped)
        print(self.stack2)
        return self.stack2.pop()


my_queue = Queue()

my_queue.push(3)
my_queue.push(2)
my_queue.push(6)
my_queue.push(4)

#print(str(my_queue))
my_queue.pop()




        