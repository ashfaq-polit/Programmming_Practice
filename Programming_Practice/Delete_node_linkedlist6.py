#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    
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
            
    def delete_element_end(self):
        if self.head == None:
            return
        else:
            temp = self.head 
            while (temp.next!= None):
                temp_prev = temp
                temp = temp.next 
            temp_prev.next = None
            
    def delete_element_beginning(self):
        if self.head == None:
            return
        else:
            temp = self.head 
            temp_next = temp.next 
            self.head = temp_next 
            temp.next = None
            
    def delete_nth_element(self, n):
        if self.head == None:
            return
        else:
            temp = self.head
            count = 1
            while (count<n):
                temp_prev = temp
                temp = temp.next 
                count+=1
            temp_prev.next = temp.next
            temp.next = None
            
    def delete_nth_element_from_end(self, n):
        if self.head == None:
            return
        else:
            temp = self.head
            count = 0
            while (temp!=None):
                temp = temp.next 
                count+=1
            length = count 
            print(count)
            n_end = length - n +1
            
            count_=1
            temp_ = self.head
            while (count_ < n_end):
                temp_prev = temp_
                temp_ = temp_.next 
                count_+=1
            temp_prev.next = temp_.next 
            temp_.next = None
            
            
    def traverse(self):
        if self.head == None:
           print('No element')
        else:
            temp = self.head
            while (temp!=None):
                print(temp.data)
                temp = temp.next
            
                       
llist = LinkedList()
llist.push_element_beginning(10)
llist.push_element_beginning(29)
llist.push_element_beginning(33)
llist.push_element_beginning(67)

llist.delete_element_end()

llist.delete_element_beginning()

llist.delete_nth_element(3)
llist.delete_nth_element_from_end(3)

llist.traverse()