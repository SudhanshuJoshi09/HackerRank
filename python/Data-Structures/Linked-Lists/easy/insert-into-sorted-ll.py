#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    if head.data > data:
        new_node = DoublyLinkedListNode(data)
        new_node.next = head
        head.prev = new_node
        new_node.prev = None
        return new_node
    
    t_head = head
    t_head_prev = head
    while t_head and t_head.data < data:
        t_head_prev = t_head
        t_head = t_head.next
        
    new_node = DoublyLinkedListNode(data)
    new_node.next = t_head
    
    if t_head is not None:
        new_node.prev = t_head.prev
        t_head.prev = new_node
    else:
        new_node.prev = t_head_prev
        
    t_head_prev.next = new_node
    
    return head

if __name__ == '__main__':