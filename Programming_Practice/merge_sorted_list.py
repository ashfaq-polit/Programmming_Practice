#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""

A = [2, 3, 6]
B = [1, 4, 7]
C = []

i=0
j=0

while i<len(A) and j<len(B):
    if A[i] <= B[j]:
        C.append(A[i])
        i+=1
    else:
        C.append(B[j])
        j+=1
        
while i<len(A):
    C.append(A[i])
    i+=1
    
        
while j<len(B):
    C.append(B[j])
    j+=1
    
print(C)

###########Linked list approach
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push_element_end(self,new_element):
        if self.head == None:
            self.head = Node(new_element)
        else:
            temp = self.head
            while(temp.next!= None):
                temp = temp.next 
            newNode = Node(new_element)
            temp.next = newNode
                                              
    def traverse(self):
        if self.head == None:
            print("No element in the list")
        else:
            temp = self.head  
            while (temp!= None):
                print(temp.data)
                temp = temp.next
                
def merge_2_sorted_list(P, Q):
    dummy = Node(0)
    tail = dummy

    while True:
        if P is None:
            tail.next = Q
            break
        if Q is None:
            tail.next = P
            break
        if P.data <= Q.data:
            tail.next = P
            P = P.next 
        #tail = tail.next
            
        else:
            # P.data > Q.data:
            tail.next = Q
            Q = Q.next 
        tail = tail.next
        
    # if Q:
    #     tail.next = Q
    # elif P:
    #     tail.next = P
    return dummy.next
    
def mergeLists(headA, headB):
  
    # A dummy node to store the result
    dummyNode = Node(0)
  
    # Tail stores the last node
    temp = dummyNode
    while True:
  
        # If any of the list gets completely empty
        # directly join all the elements of the other list
        if headA is None:
            temp.next = headB
            break
        if headB is None:
            temp.next = headA
            break
  
        # Compare the data of the lists and whichever is smaller is
        # appended to the last of the merged list and the head is changed
        if headA.data <= headB.data:
            temp.next = headA
            headA = headA.next
        else:
            temp.next = headB
            headB = headB.next
  
        # Advance the temp
        temp = temp.next
  
    # Returns the head of the merged list
    return dummyNode.next
            
P = LinkedList()
P.push_element_end(1)
P.push_element_end(2)
P.push_element_end(4)

Q = LinkedList()
Q.push_element_end(1)
Q.push_element_end(3)
Q.push_element_end(4)

P.traverse()
Q.traverse()

P.head = merge_2_sorted_list(P.head,Q.head)
P.head = mergeLists(P.head, Q.head)
        
        