#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:52:04 2020

@author: vivian
"""

""" Individual assignment: Linked List

Our assignment was to:
    1. Create a linked list with OOP tools, which includes:
        a. defining a class node 
        b. givign reference about what is the next element
        c. inserting new elements right after the head
    
    2. Proving constant time complexitiy by trying differently sized lists:
        a. (measure time complexity for this in general)
    
    3. Share on Github or Gitlab and upload as .py file on canvas       """

""" My solution"""



""" 1) Importing libaries """


import numpy as np # libary, which we need to create random arrays in different sizes
import pandas as pd # libary, which we need to visualize our time complexity later



""" 2) Creating random arrays """

# create arrays of different sizes, which we want to turn into nodes of a linked list
array_to_nodes_1 = np.random.randint (1, 100, 10) 
array_to_nodes_2 = np.random.randint (1, 5, 100)
array_to_nodes_3 = np.random.randint (1, 5, 1000)

# check if arrays look like expected
print (array_to_nodes_1)
print (array_to_nodes_2)
print (array_to_nodes_3)



""" 3) Defining a Node Class """


class CreateDataTypeNode:    # creating data structure for nodes and their corresponding list
    def __init__(self, data): # initializing object with init_function
        self.data = data   # create "data container"
        self.next = None  # create pointer to next node
        return


    
""" 4) Defining a Linked List Class including different methods """



class LinkedList: # now we are creating methods we need for linked lists
    def __init__(self): # initialize object with init_function
        self.head = None # first empty so we can add nodes later
        self.tail = None # hence nodes both at beginning and end (head & tail) are "None"
        
        return
    
    
    def add_node_to_list (self, node): # adding nodes at the end of the list 
        if not isinstance(node, CreateDataTypeNode): # checks if item has node-character
            node = CreateDataTypeNode (node) # if not it creates a node 
    
        if self.head is None: # if head is empty we make the new node head
            self.head = node
        else: 
            self.tail.next = node # if not we add new node behind last node at tail
        
        
        self.tail = node
        
        return
    
    
    def length_of_linkedlist(self): # counts numbers of nodes in linked list
        count = 0  # supposed to start counting at zeroth element
        node_to_be_count = self.head # beginning of the to be counted node is the head-node
  
# for while loop: if current node is not null ('none') it has a node that's next,
# which is why we have to tell the algorithm it has to check the next node as well


        while node_to_be_count is not None: 
            count = count + 1
        
            # since the 'old' node is now counted we need to jump 
            # to the next node, which needs to be counted
            node_to_be_count = node_to_be_count.next 
        
        return count 



""" 5) Making conversion visible """


track = LinkedList()

for node_to_be_count in array_to_nodes_1:
    track.add_node_to_list(node_to_be_count)
    print ("track length: %i" % track.length_of_linkedlist())


for node_to_be_count in array_to_nodes_2:
    track.add_node_to_list (node_to_be_count)
    print ("track length: %i" % track.length_of_linkedlist())


for node_to_be_count in array_to_nodes_3:
    track.add_node_to_list (node_to_be_count)
    print ("track length: %i" % track.length_of_linkedlist())


    
""" 6) Measuring time complexity """


