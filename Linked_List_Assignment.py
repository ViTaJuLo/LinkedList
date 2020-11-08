#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
""" Linked_List """

class Node:

    def __init__(self, data): 
        self.data = data
        self.next = None

    def insert_next(self, node): 
        node.next = self.next
        self.next = node

    def insert_at_position(self, node, position):
        i = 0
        next_node = self.next
        while i <= position -4:
            i = i + 1
            next_node = next_node.next
        next_node.insert_next(node)

    def return_as_list(self):
        node_data = []
        current = self
        while (current.next):
            node_data.append(current.data)
            current = current.next
        node_data.append(current.data)
        return node_data

""" Creating Linked List """

def createlinkedlistofthrees(number_of_nodes):
    head = Node(3)
    i = 0
    end = head
    while  i <= number_of_nodes -2:
        i = i + 1
        x = Node(3)
        end.next = x
        end = x
    return head


linkedlist_1000 = createlinkedlistofthrees(1000)
linkedlist_100000 = createlinkedlistofthrees(100000)

""" Showing constant time complexity for insertion """

import time 

i = 0
while i <= 100:
    i = i +1
    start = time.time()
    linkedlist_1000.insert_next(Node(4))
    elapse1 = time.time() - start
    start = time.time()
    linkedlist_100000.insert_next(Node(4))
    elapse2 = time.time() - start
 
    print ( elapse1*1000 , elapse2*1000 )
   

print("finish")



