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
            
    def push_element_end(self,new_element):
        if self.head == None:
            self.head = Node(new_element)
        else:
            temp = self.head
            while(temp.next!= None):
                temp = temp.next 
            newNode = Node(new_element)
            #newNode.next = None
            temp.next = newNode
            
    def push_element_nth(self, new_element, n):
        if self.head == None:
            self.head = Node(new_element)
        else:
            count =1
            newNode = Node(new_element)
            temp = self.head  
            while (count < n):
                temp_prev = temp
                temp = temp.next 
                count+=1
            newNode.next = temp_prev.next 
            temp_prev.next = newNode
                
                        
    def find_element_linkedlist(self, element):
        if self.head == None:
            return
        else:
            temp = self.head
            while (temp!=None):
                if temp.data == element:
                    print('Found')
                    return
                else:
                    temp = temp.next
            print('Not Found')
            
    def print_middle_element(self):
        if self.head == None:
            return
        else:
            temp = self.head
            count = 0
            while (temp != None):
                count += 1
                temp = temp.next
            mid = count // 2
            print(mid)
            temp2 = self.head 
            count1 = 0
            while (count1 < mid):
                count1 += 1
                temp2 = temp2.next 
            print(temp2.data)
                
            
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

llist.push_element_end(40)
llist.push_element_end(73)
llist.push_element_nth(88, 3)

llist.find_element_linkedlist(40)


llist.print_middle_element()

llist.traverse()
    
