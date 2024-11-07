#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push_element_beginning(self, new_element):
        if self.head == None:
           self.head = Node(new_element)
        else:
            newNode = Node(new_element)
            newNode.next = self.head
            self.head = newNode
    
    def reverse(self):
        if self.head == None:
            return
        else:
            temp_prev = None
            temp = self.head 
            temp_next = self.head 
            while (temp != None):
                temp_next = temp_next.next 
                temp.next = temp_prev 
                temp_prev = temp 
                temp = temp_next 
            self.head = temp_prev
            
    def circular(self):
        if self.head == None:
            return
        else:
            slow = self.head 
            fast= self.head
            while (fast != None and fast.next != None):
                slow = slow.next 
                fast= fast.next.next
                if slow == fast:
                    return True
            return False
    
                    
                               
    def traverse(self):
        if self.head == None:
            print("No element in the list")
        else:
            temp = self.head  
            while (temp!= None):
                print(temp.data)
                temp = temp.next
                
llist = LinkedList()
llist.push_element_beginning(10)
llist.push_element_beginning(20)
llist.push_element_beginning(33)
llist.push_element_beginning(44)

llist.head.next.next.next.next = llist.head.next

llist.reverse()


if(llist.circular_pos(2)):
    print("Loop found")
else:
    print("No Loop ")

llist.traverse()

    